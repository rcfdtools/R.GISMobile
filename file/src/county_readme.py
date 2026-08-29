# https://github.com/rcfdtools
# -*- coding: UTF-8 -*-
# Markdown report of individual county layers in /shp


# Libraries
import functions as funcs
from pathlib import Path
from pandas.core.interchange.from_dataframe import primitive_column_to_ndarray
from simpledbf import Dbf5
import tabulate
import matplotlib.pyplot as plt
import pandas as pd
pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# Processing
url_file = 'https://github.com/rcfdtools/R.GISMobile/blob/main/file/shp/'
dir_path = Path('../shp')
create_location_map = True # ● Create and save location map
print_on_screen = False # Global print graph in screen
zip_files = [file.name for file in dir_path.glob('*.zip')]
file_log_name = f'../shp/Readme.md'  # Markdown file log
file_log = open(file_log_name, 'w+', encoding='utf-8')  # w+ create the file if it doesn't exist
# County list
dbf_county = Dbf5('../shp/ColombiaCounty4326.dbf', codec='cp1252')
df_county = pd.DataFrame(dbf_county.to_dataframe())
df_county = df_county[['DeCodigo', 'DeNombre', 'MpCodigo', 'MpNombre', 'MpNorma', 'Latitude', 'Longitude']]
df_county = df_county.sort_values(by=['DeCodigo', 'DeNombre', 'MpNombre', 'MpCodigo'])
df_county.drop(df_county[df_county['MpCodigo'] == '00000'].index, inplace=True)
# State list
df_state = df_county['DeCodigo'].unique()
funcs.print_log(file_log, f'<div align="center"><img alt="rcfdtools" src="../graph/R.GISMobile.svg" width="300px"></div>\n\n')
funcs.print_log(file_log, f'# 🌎County Layer - Colombia South America')
for state in df_state:
    print_dataframe = pd.DataFrame(columns=['CountyID', 'CountyName', 'CountyFiles'])
    df_state_info = df_county[df_county['DeCodigo'] == state]
    state_name = df_state_info['DeNombre'].values[0]
    df_county_filter = df_county[df_county['DeCodigo'] == state]
    state_latitude = df_state_info['Latitude'].values[0]
    state_longitude = df_state_info['Longitude'].values[0]
    funcs.print_log(file_log, f'\n\n\n# {state} - {state_name} ({len(df_county_filter)} Counties)\n')
    fig_file0a = '../graph/' + state + 'LocationMap.png'
    if create_location_map:
        location_map_plot = funcs.location_map(point_latitude = state_latitude, point_longitude = state_longitude, point_name = state_name.upper(), state_filter = state, county_label_on = True)
        location_map_plot.savefig(fig_file0a, dpi=120)
        plt.close()
    funcs.print_log(file_log, f'<img alt="rcfdtools" src="{fig_file0a}" width="500"></img>', center_div=True, on_screen=print_on_screen)
    df_county_unique = df_county_filter['MpCodigo'].unique()
    for county in df_county_unique:
        df_county_info = df_county[df_county['MpCodigo'] == county]
        county_name = df_county_info['MpNombre'].values[0]
        zip_files_filter = [item for item in zip_files if item.startswith(county)]
        files_txt = ''
        if len(zip_files_filter) > 0:
            for file in zip_files_filter:
                files_txt += f'[{file}]({url_file}{file})<br/>'
        else:
            files_txt = 'Not found'
        print_dataframe.loc[len(print_dataframe)] = [county, county_name, files_txt]
    funcs.print_log(file_log, print_dataframe.to_markdown(index=False), center_div=True)
