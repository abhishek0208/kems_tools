import os, sys
import subprocess
from numpy.lib.shape_base import expand_dims
import pandas as pd
import json
from pandas.io.json import json_normalize
import numpy as np
import time
pd.__version__

output_folder = r'C:\Users\abhis\Google Drive\Kuungana Advisory_South Sudan\Model files\Model runs\14092021_v1\JSON'
csv_folder = r'C:\Users\abhis\Google Drive\Kuungana Advisory_South Sudan\Model files\Model runs\14092021_v3\CSV'

final_df = pd.DataFrame(columns=['Year','Month', 'Day','Hour','Generator','Resource','Variable','Value'],
                        dtype=object)

file_count = 0
start = time.process_time()

for each_json in os.listdir(output_folder):
    file_count += 1
    print('Processing ', 
          file_count, 
          ' out of ', 
          len(os.listdir(output_folder)),
          ' files')
    with open(os.path.join(output_folder,
                           each_json)) as json_data:
        data = json.load(json_data)

    # Flatten JSON
    pd.json_normalize(data, 'Solution', ['Variable'], errors='ignore')
    df = pd.DataFrame(data['Solution'])

    # Create dictionary with variable-value combinations
    variables_dict = dict(df['Variable'])
    del variables_dict[0]

    # Create DataFrame from variable-values dictionary 
    df = pd.DataFrame.from_dict(variables_dict).reset_index()
    df.columns = ['Variables', 'Values']

    # Add columns for year, month, and day based on JSON filename 
    df['Year'] = each_json.split('_')[1].split('.')[0][0:4]
    df['Month'] = each_json.split('_')[1].split('.')[0][4:6]
    df['Day'] = each_json.split('_')[1].split('.')[0][6:8]

    # Split 'Variables' column
    df[['Variable', 'Indices']] = df['Variables'].str.split('[',
                                                            expand=True)
    df['Indices'] = df['Indices'].str.rstrip(']')
    df['Value'] = df['Values'].apply(lambda x: x['Value'])
    df.drop(columns=['Variables','Values'], 
            inplace=True)

    # Insert empty columns
    df.insert(3, 'Hour', '')
    df.insert(4, 'Generator', '')
    df.insert(5, 'Resource', '')

    # Create dictionary of variable-index combinations
    variable_columns = {'CapacityFactor': ['Generator', 'Hour'],
                        'FuelCostByGenerator': ['Generator', 'Resource', 'Hour'],
                        'FuelCostByUnitByGenerator': ['Generator', 'Resource'],
                        'FuelCostTotal': ['Resource', 'Hour'],
                        'GenerationSystem': ['Hour'],
                        'Generation': ['Generator', 'Hour'],
                        'NonFuelVariableCostByGenerator': ['Generator', 'Hour'],
                        'NonFuelVariableCostByUnitByGenerator': ['Generator'],
                        'NonFuelVariableCostTotal': ['Hour'],
                        'ResourceConsumptionByGenerator': ['Generator', 'Resource', 'Hour'],
                        'ResourceConsumptionTotal': ['Resource', 'Hour'],
                        'ShortRunMarginalCostByGenerator': ['Generator'],
                        'TotalCost': ['Hour'],
                        'UnservedEnergy': ['Hour']}

    # Loop through each index of each variable 
    for each_variable in variable_columns.keys():
        index_count = 0

        for each_index in variable_columns[each_variable]:
            df.loc[df['Variable'] == each_variable,
                   each_index] = (df[df['Variable'] == each_variable]['Indices']
                                  .str.split(',', expand=True)[index_count])
            index_count += 1

    # Split CapacityFactor
    # df[['Generator', 'Hour']] = (df[df['Variable'] == 'CapacityFactor']['Indices']
    #                             .str.split(',',
    #                                        expand=True))

    '''
    df.loc[df['Variable'] == 'CapacityFactor',
           'Generator'] = (df[df['Variable'] == 'CapacityFactor']['Indices']
                                                           .str.split(',', expand=True)[0])
    df.loc[df['Variable'] == 'CapacityFactor',
           'Hour'] = (df[df['Variable'] == 'CapacityFactor']['Indices']
                                                      .str.split(',', expand=True)[1])
    '''
    df.drop(columns=['Indices'],
            inplace=True)

    # Concatenate dataframes
    final_df = pd.concat([final_df,
                          df])

# Print
final_df.to_csv(os.path.join(csv_folder,
                           'OptimisationResults_final.csv'),
              index=False)

print('Process took ', 
      time.process_time() - start, 
      ' seconds')
