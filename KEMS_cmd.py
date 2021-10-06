import os, sys
import subprocess
import pandas as pd
pd.__version__

input_folder = r'C:\Users\abhis\Google Drive\Kuungana Advisory_South Sudan\Model files\Model runs\14092021_v3\DAT'
output_folder = r'C:\Users\abhis\Google Drive\Kuungana Advisory_South Sudan\Model files\Model runs\14092021_v3\JSON'
model_file = r'C:\Users\abhis\Google Drive\Kuungana Advisory_South Sudan\Model files\KEMS-Dispatch_v1_3.py'
solver = 'cbc'

for each_dat in os.listdir(input_folder):
    each_json = ('OptimisationResults_' +
                 each_dat.split('_')[1].split('.')[0] +
                 '.json')
    each_csv = ('OptimisationResults_' +
                 each_dat.split('_')[1].split('.')[0] +
                 '.csv')

    pyomo_command = ('pyomo solve ' +
                     '--solver=' +
                     solver +
                     ' "' +
                     model_file +
                     '" "' +
                     input_folder + '\\' + each_dat +
                     '" ' +
                     '--save-results "' +
                     output_folder + '\\' + each_json +
                     '"')
    subprocess.Popen('start /wait ' + 
                     pyomo_command, 
                     shell=True, 
                     cwd=os.getcwd()).wait()    
    print(pyomo_command)


