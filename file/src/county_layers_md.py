# https://github.com/rcfdtools
# -*- coding: UTF-8 -*-
# Markdown report of individual county layers in /shp


# Libraries
from pathlib import Path
from simpledbf import Dbf5
import tabulate
import pandas as pd
pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# Function for print and show results in a log file
def print_log(file_log, txt_print, on_screen=False, center_div=False):
    # div50 is use for show 2 plots in the same line
    if on_screen:
        print(txt_print)
    if center_div:
        file_log.write('\n<div align="center">\n' + '\n')
    file_log.write(txt_print)
    if center_div:
        file_log.write('\n\n</div>\n' + '\n')

# Processing
url_file = 'https://github.com/rcfdtools/R.GISMobile/blob/main/file/shp/'
dir_path = Path('../shp')
zip_files = [file.name for file in dir_path.glob('*.zip')]
file_log_name = f'../shp/Readme.md'  # Markdown file log
file_log = open(file_log_name, 'w+', encoding='utf-8')  # w+ create the file if it doesn't exist
dbf_county = Dbf5('../shp/ColombiaCounty4326.dbf', codec='cp1252')
df_county = pd.DataFrame(dbf_county.to_dataframe())
df_county = df_county[['DeCodigo', 'DeNombre', 'MpCodigo', 'MpNombre', 'MpNorma', 'Latitude', 'Longitude']]
df_county = df_county.sort_values(by=['DeCodigo', 'DeNombre', 'MpCodigo', 'MpNombre'])
df_county.drop(df_county[df_county['MpCodigo'] == '00000'].index, inplace=True)
grouped = df_county.groupby('MpCodigo')
print_log(file_log, f'<div align="center"><img alt="rcfdtools" src="../graph/R.GISMobile.svg" width="300px"></div>\n\n')
print_log(file_log, f'# 🌎GISMobile: Layers por Municipio - Colombia Suramérica\n')
for group_id, group_df in grouped:
    df_county_info = df_county[df_county['MpCodigo'] == group_id]
    state_name = df_county_info['DeNombre'].values[0]
    county_name = df_county_info['MpNombre'].values[0]
    print_log(file_log,f'\n\n**{state_name} / {county_name}** ({group_id}): ')
    #zip_files_filter = [item for item in zip_files if group_id in item]
    zip_files_filter = [item for item in zip_files if item.startswith(group_id)]
    if len(zip_files_filter) > 0:
        for file in zip_files_filter:
            print_log(file_log,f'[•{file}]({url_file}{file}) ')
    else:
        print_log(file_log,'layers not found in county')
