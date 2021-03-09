
# Importing required libraries
import sys, os, shutil

from jproperties import Properties

# Loading properties file for default settings to split output file
configs = Properties()
with open('raman-config.properties', 'rb') as config_file:
    configs.load(config_file)

# Reading Config Properties file data
input_file= configs.get("INPUT_FILE_NAME").data
data_prefix = configs.get("DATA_PREFIX").data
data_suffix = configs.get("DATA_SUFFIX").data
data_join_glue = configs.get("DATA_GLUE").data
split_file_size_int = int(configs.get("SPLIT_FILE_SIZE").data)


# Getting current working directory
pathname = os.path.dirname(sys.argv[0])

# Displaying welcome message (FEATURES, Getting Started, DEFAULT SETTINGS USED)
print("\n*********************************Welcome to Excel input data splitter**************************")
print("\t\t1. FEATURES: This script will Remove empty lines, Trim spaces from both sides of input data and Remove Duplicates.\n")
print('\t=================================================================================================')
print(f"\t\t2. GET STARTED: To start please copy the input data column from excel file to {input_file} in below format:- ")
print("\t\t091KOLK1143035276478")
print("\t\t091BANG623029385965")
print("\t\t091NOID623033006522")
print("\t\t....\n")
print('\t=================================================================================================')
print(f"\t\t3. DEFAULT SETTINGS USED: Can be changed by editing 'raman-config.properties' file in path: {os.path.abspath(pathname)}")
print(f'\t\tINPUT_FILE_NAME = {input_file}')
print(f'\t\tSPLIT_FILE_SIZE = {split_file_size_int} entries per output file')
print(f'\t\tDATA_PREFIX = {data_prefix}')
print(f'\t\tDATA_SUFFIX = {data_suffix}')
print(f'\t\tDATA_GLUE = {data_join_glue}')
print('\t\tFORMATT             ==>  Data_prefix + Data + Data_suffix + Data_glue')
print(f'\t\tData output preview ==> {data_prefix} 091HYDE030030834214 {data_suffix} {data_join_glue}')
print("***********************************************************************************************\n\n")

# Function to read input file for generating split output file
def read_input_file():
    # Read file into DS
    with open(input_file) as f:
        # perform file operations
        return f.read()

# Reading input data into string
input_data=read_input_file()

# Performing E+ number formatting check
if('+' in input_data):
    print("***********************************************************************************************")
    print("         Warning: Input data contains plus('+') sign, maybe long number is wrongly copied (Example- '114021513531513155' in excel copied as '11.40215e+14').")
    print("\t\tTo correct, please read below note: ")
    print("\t\t1. After copying data from excel, paste it in new excel file by selecting whole column > 'Format' > 'Custom' > Second option as '0' ")
    print(f"\t\t2. Paste and then re-copy to input txt file: {input_file}\n\n")
    input("Press enter to continue after doing changes...")
    # Reading again after + sign removal
    input_data=read_input_file()

input_data_cleaned_stage3=[]
# Funtion for Cleaning Read Input Data 
def clean_input_data(input_read_data):
    # Removing Trailing Whitespaces and Making into a List
    input_data_cleaned_stage1=[str.strip() for str in input_read_data.splitlines()]

    # Removing Empty Lines
    input_data_cleaned_stage2 = list(filter(bool, input_data_cleaned_stage1))

    # Removing Duplicates
    for word in input_data_cleaned_stage2:
        if word not in input_data_cleaned_stage3:
            input_data_cleaned_stage3.append(word)
    
    return input_data_cleaned_stage3

# Cleaning input data
input_data_cleaned_stage3=clean_input_data(input_data)

# Getting Total Input data size
total_input_data_size=len(input_data_cleaned_stage3)

# Calculating number of split output files to be created
no_of_files=total_input_data_size//split_file_size_int
if(total_input_data_size > no_of_files * split_file_size_int):
    no_of_files = no_of_files + 1

#Preview of output data
print("\n\nPreview of output data:- ")
for word in input_data_cleaned_stage3[:10]:
    print(data_prefix + word + data_suffix + data_join_glue, end='')
print(f'... +{total_input_data_size-10} more row(s) to be splitted in {no_of_files} file(s)')
print(f'{total_input_data_size} Total size\n\n')

# Confirming from user to Delete previous output files and Prepare split output files
input("Delete previous output files? Press enter to continue...")

# Reading again to read any changes done after showing preview
input_data=read_input_file()
input_data_cleaned_stage3=clean_input_data(input_data)

# Deleting previous output files from output folder
folder = 'output folder'
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))
print('Deleted previous output files. ', end='')

# Creating output folder if not created
try:
    os.mkdir('output folder')
except OSError as error:
    print('Output Folder is created.')

# Creating split output files for required number of input
count=0
for x in range(0, total_input_data_size, split_file_size_int):
    f=open('output folder/output'+str(count+1)+'.txt','w')
    s1 = (data_join_glue.join(data_prefix + item + data_suffix for item in input_data_cleaned_stage3[count*split_file_size_int:(count+1)*split_file_size_int]))
    count=count+1
    f.write(s1)
    f.close()

# Finished
print('\nDONE!!!!!!')