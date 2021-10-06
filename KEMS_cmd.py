import os, sys
import subprocess
import pandas as pd
import time
pd.__version__

input_folder = r'C:\Users\abhis\Google Drive\Kuungana Advisory_South Sudan\Model files\Model runs\06102021_v1\DAT'
output_folder = r'C:\Users\abhis\Google Drive\Kuungana Advisory_South Sudan\Model files\Model runs\06102021_v1\JSON'
model_file = r'C:\Users\abhis\Google Drive\Kuungana Advisory_South Sudan\Model files\KEMS-Dispatch_v1_3.py'
solver = 'glpk'

start = time.process_time()
file_count = 0

for each_dat in os.listdir(input_folder):
    file_count += 1
    print('Processing ', 
          file_count, 
          ' out of ', 
          len(os.listdir(input_folder)),
          ' files')
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

print('Process took ',
      time.process_time() - start,
      ' seconds')
