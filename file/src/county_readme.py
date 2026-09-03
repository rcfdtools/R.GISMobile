# https://github.com/rcfdtools
# -*- coding: UTF-8 -*-
# Markdown report of individual county layers in /shp

# Libraries
import functions as funcs
import dictionary as dictionary
from pathlib import Path
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
ppsd_link = 'https://github.com/rcfdtools/R.HydroTools/blob/main/tool/Population/file/report/'
country_code = '57'
minimap_link = 'https://github.com/rcfdtools/R.GISMobile/blob/main/file/gis/MiniMap/'
county_layer_path = '../gis/CountyLayer_Co/'
county_layer_filetype_path = f'{county_layer_path}county_layer_filetype.csv'
dir_path = Path('../shp')
print_on_screen = False # Global print graph in screen
zip_files = [file.name for file in dir_path.glob('*.zip')]
file_log_name = f'{county_layer_path}/Readme.md'  # Markdown file log
file_log = open(file_log_name, 'w+', encoding='utf-8')  # w+ create the file if it doesn't exist
# County list
dbf_county = Dbf5(f'{dir_path}/ColombiaCounty4326.dbf', codec='cp1252')
df_county = pd.DataFrame(dbf_county.to_dataframe())
df_county = df_county[['DeCodigo', 'DeNombre', 'MpCodigo', 'MpNombre', 'MpNorma', 'Latitude', 'Longitude']]
df_county = df_county.sort_values(by=['DeCodigo', 'DeNombre', 'MpNombre', 'MpCodigo'])
df_county.drop(df_county[df_county['MpCodigo'] == '00000'].index, inplace=True)
# Filetype list
df_county_layer_filetype = pd.read_csv(county_layer_filetype_path, encoding='cp1252', sep=',', dtype={'FileName': 'str', 'EnDesc': 'str', 'EsDesc': 'str'})
#print(df_county_layer_filetype.to_markdown(index=False))
# State list
df_state = df_county['DeCodigo'].unique()

# Main Readme.md
funcs.print_log(file_log, f'<div align="center"><img alt="rcfdtools" src="../../graph/R.GISMobile.svg" width="250px"></div>\n\n')
funcs.print_log(file_log, f'# _{dictionary.dicts['study_name']}_ \n{dictionary.dicts['keywords']}\n\n{dictionary.dicts['study_desc']}\n\n\n', on_screen=print_on_screen)
funcs.print_log(file_log, f'## File names\n\n{dictionary.dicts['county_layer_filetype']}\n\n{df_county_layer_filetype.to_markdown(index=False)}\n\n\n## Colombian States\n\n{dictionary.dicts['state']}\n', on_screen=print_on_screen)
for state in df_state:
    df_state_info = df_county[df_county['DeCodigo'] == state]
    state_name = df_state_info['DeNombre'].values[0]
    df_county_filter = df_county[df_county['DeCodigo'] == state]
    funcs.print_log(file_log, f'\n* [{state} - {state_name}]({state}.md) ({len(df_county_filter)} Counties)')
funcs.print_log(file_log, f'\n\n#\n\n<div align="center"><img alt="rcfdtools" src="../../graph/qr-code-shp.png" width="250px"><br><sub>Share this research</sub></div><br>', on_screen=print_on_screen)
funcs.print_log(file_log, f'\n\n<sub>{dictionary.dicts['disclaimer']}</sub>', on_screen=print_on_screen)
funcs.print_log(file_log, f'\n\n| [:house: Home](../../../README.md)  | [:beginner: Help / Collab](https://github.com/rcfdtools/R.GISMobile/discussions) |', on_screen=print_on_screen)
funcs.print_log(file_log, f'\n|----------------------------|-------------------------------------------------------------------------------------------|', on_screen=print_on_screen)

# Individual state.md readme files
for state in df_state:
    file_log_name = f'{county_layer_path}/{state}.md'  # Markdown file log
    file_log = open(file_log_name, 'w+', encoding='utf-8')  # w+ create the file if it doesn't exist
    print_dataframe = pd.DataFrame(columns=['MiniMap', 'CountyID', 'CountyName', 'CountyFiles'])
    df_state_info = df_county[df_county['DeCodigo'] == state]
    state_name = df_state_info['DeNombre'].values[0]
    df_county_filter = df_county[df_county['DeCodigo'] == state]
    funcs.print_log(file_log, f'<div align="center"><img alt="rcfdtools" src="../../graph/R.GISMobile.svg" width="250px"></div>\n\n')
    funcs.print_log(file_log, f'# _{dictionary.dicts['study_name']} for {state} - {state_name} ({len(df_county_filter)} Counties)_ \n{dictionary.dicts['keywords']}\n\n{dictionary.dicts['study_desc']}\n\n', on_screen=print_on_screen)
    state_latitude = df_state_info['Latitude'].values[0]
    state_longitude = df_state_info['Longitude'].values[0]
    #funcs.print_log(file_log, f'\n# {state} - {state_name} ({len(df_county_filter)} Counties)\n')
    fig_file0a = f'{minimap_link}{country_code}_{state}_MiniMap.png'
    funcs.print_log(file_log, f'<img alt="rcfdtools" src="{fig_file0a}" width="600px"></img>', center_div=True, on_screen=print_on_screen)
    df_county_unique = df_county_filter['MpCodigo'].unique()
    for county in df_county_unique:
        df_county_info = df_county[df_county['MpCodigo'] == county]
        df_county_info['MpNorma'] = df_county_info['MpNorma'].fillna('')
        county_name = df_county_info['MpNombre'].values[0]
        county_ppsd_link = f'[{str(county)}]({ppsd_link}{str(county)}.md)'
        county_minimap = f'<img alt="rcfdtools" src="{minimap_link}{country_code}_{str(county)}_MiniMapCountySimple.png" height="150px">'
        zip_files_filter = [item for item in zip_files if item.startswith(county)]
        files_txt = ''
        if len(zip_files_filter) > 0:
            for file in zip_files_filter:
                files_txt += f'[{file}]({url_file}{file})<br/>'
        else:
            files_txt = 'Not found'
        print_dataframe.loc[len(print_dataframe)] = [county_minimap, county_ppsd_link, county_name, files_txt]
    funcs.print_log(file_log, print_dataframe.to_markdown(index=False), center_div=True)
    funcs.print_log(file_log, f'\n#\n\n<div align="center"><img alt="rcfdtools" src="../../graph/qr-code-shp.png" width="250px"><br><sub>Share this research</sub></div><br>', on_screen = print_on_screen)
    funcs.print_log(file_log, f'\n\n<sub>{dictionary.dicts['disclaimer']}</sub>', on_screen = print_on_screen)
    funcs.print_log(file_log, f'\n\n| [:house: Home](Readme.md)  | [:beginner: Help / Collab](https://github.com/rcfdtools/R.GISMobile/discussions) |', on_screen=print_on_screen)
    funcs.print_log(file_log, f'\n|----------------------------|-------------------------------------------------------------------------------------------|', on_screen=print_on_screen)
