# Split_Excel_Input_Data_To_1000_Oracle_SQL

This python 3 script helps to Split Excel Column data in pieces of 1000 data points so that it can be easily queried via Oracle SQL Database Query without facing following error:

![image](https://user-images.githubusercontent.com/26063397/110437041-f2394f00-80da-11eb-84ae-b8bb50b016d6.png)

> ORA-01795: maximum number of expressions in a list is 1000
> 01795. 00000 -  "maximum number of expressions in a list is 1000"
> *Cause:    Number of expressions in the query exceeded than 1000.
>            Note that unused column/expressions are also counted
>            Maximum number of expressions that are allowed are 1000.
>*Action:   Reduce the number of expressions in the list and resubmit.
>Error at Line: 317 Column: 38

and it will Remove empty lines, Trim spaces from both sides of input data cell and Remove Duplicates.


## Welcome to Excel input data splitter
### 1. FEATURES: This script will Remove empty lines, Trim spaces from both sides of input data and Remove Duplicates.

### 2. GET STARTED: To start please copy the input data column from excel file to input.txt in below format:-
                091BHARAT3035276478
                091SITA623029385965
                091LAXMI23033006522
                ....

### 3. DEFAULT SETTINGS USED: Can be changed by editing 'raman-config.properties' file in relative path: 
                INPUT_FILE_NAME = input.txt
                SPLIT_FILE_SIZE = 1000 entries per output file
                DATA_PREFIX = '
                DATA_SUFFIX = '
                DATA_GLUE = ,

                FORMATT              ==>  Data_prefix + Data + Data_suffix + Data_glue
                Data output preview ==> ' 091RAMA030030834214 ' ,
![image](https://user-images.githubusercontent.com/26063397/110439536-96bc9080-80dd-11eb-839f-ba0deda05f79.png)

### DEMO:
1. Copy the input to the input.txt file.
    ![image](https://user-images.githubusercontent.com/26063397/110438561-822bc880-80dc-11eb-8bb2-6f3b0299cf1c.png)
2. Run python script given **split_thousand.py** file
    
    > python split_thousand.py
    
    ![image](https://user-images.githubusercontent.com/26063397/110435008-7fc76f80-80d8-11eb-8ea3-613f89143259.png)
    
    Done!
    ![image](https://user-images.githubusercontent.com/26063397/110435335-e6e52400-80d8-11eb-81c2-876275590762.png)

    **Note: Python 3 should be installed in your system with shutil and jproperties**
    
    a. pip install jproperties ([jproperties install guide](https://pypi.org/project/jproperties/))

3. Output will be saved in **output folder** folder.
    ![image](https://user-images.githubusercontent.com/26063397/110436526-59a2cf00-80da-11eb-9bbe-73a2b0b91ea2.png)
