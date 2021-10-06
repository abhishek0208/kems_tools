# KEMS tools
A set of tools to work with the KEMS model. 
The packages required to run the scripts in this repo can be installed 
by running the following command on the command line:
```
pip install -r requirements.txt
```

It is recommended that the packages are installed in a newly created environment.


## 1. `KEMS_cmd.py`

This script can be used to automate the process of carrying out KEMS model runs on Pyomo.
Before running the script, update the **input_folder**, **output_folder**, and **model_file** paths in it. 
A user can also choose either **cbc** or **glpk** as the solver.  
The **input_folder** is where the set of DAT files with the input data is located and 
the **output_folder** is the user-defined destination for the result JSON files file. 
The **model_file** refers to the KEMS model in Pyomo.
The script can then be run on the command line using:
```
python KEMS_cmd.py
```

## 2. `json_to_csv.py`

This script converts and combines a set of JSON results file from KEMS model runs 
into a CSV file.

Before running the script, update the **input_folder** and **csv_folder** paths in it. 
The **input_folder** is where the set of JSON files to be converted is located and 
the **csv_folder** is the user-defined destination for the final CSV file. 
The script can then be run on the command line using:
```
python json_to_csv.py
```
