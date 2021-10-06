# KEMS tools
A set of tools to work with the KEMS model. 
The packages required to run the scripts in this repo can be installed 
by running the following command on the command line:
```
pip install -r requirements.txt
```

It is recommended that the packages are installed in a newly created environment.


## 1. `json_to_csv.py`

This script converts and combines a set of JSON results file from KEMS model runs 
into a CSV file.

Before running the script, update the **input_folder** and **csv_folder** paths in it. 
The **input_folder** is where the set of JSON files to be converted is located and 
the **csv_folder** is the user-defined destination for the final CSV file. 
The script can then be run on the command line using:
```
python json_to_csv.py
```