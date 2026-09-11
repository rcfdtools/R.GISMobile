# https://github.com/rcfdtools
# -*- coding: UTF-8 -*-
# Markdown report of individual county layers in /shp

# Libraries
import countylayer_functions as funcs
import countylayer_dictionary as dictionary
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
igac_map_sheet_link = 'https://www.colombiaenmapas.gov.co/?u=0&t=23&servicio=5&hoja='
county_layer_path = '../gis/CountyLayer_Co/'
county_layer_filetype_path = f'../table/countylayer_filetype.csv'
county_layer_economic_destination_igac_path = f'../table/countylayer_economic_destination_igac.csv'
dir_path = Path('../shp')
print_on_screen = False # Global print graph in screen
# zip_files = [file.name for file in dir_path.glob('*.zip')]
zip_files = [file.name for file in dir_path.iterdir() if file.suffix in ('.zip', '.rar')]
file_log_name = f'{county_layer_path}/Readme.md'  # Markdown file log
file_log = open(file_log_name, 'w+', encoding='utf-8')  # w+ create the file if it doesn't exist

# County list (es: Listado de municipios)
dbf_county = Dbf5(f'{dir_path}/ColombiaCounty4326.dbf', codec='cp1252')
df_county = pd.DataFrame(dbf_county.to_dataframe())
df_county = df_county[['DeCodigo', 'DeNombre', 'MpCodigo', 'MpNombre', 'MpNorma', 'Latitude', 'Longitude']]
df_county = df_county.sort_values(by=['DeCodigo', 'DeNombre', 'MpNombre', 'MpCodigo'])
df_county.drop(df_county[df_county['MpCodigo'] == '00000'].index, inplace=True)

# Cadastre manager (es: Gestor catastral)
# Date fields must be moved to Text fields and deleted in the layer before running
dbf_cadastre_manager = Dbf5(f'{dir_path}/ColombiaCadastreManager4326.dbf') # , codec='cp1252'
#print(dbf_cadastre_manager.fields)
df_cadastre_manager = pd.DataFrame(dbf_cadastre_manager.to_dataframe())
df_cadastre_manager = df_cadastre_manager[['mpcodigo', 'Cadastre']]
df_cadastre_manager = df_cadastre_manager.sort_values(by=['mpcodigo'])
df_cadastre_manager.drop(df_cadastre_manager[df_cadastre_manager['mpcodigo'] == '00000'].index, inplace=True)
#print(df_cadastre_manager)

# IGAC Map Sheets (es: Hojas cartográficas)
dbf_map_sheet = Dbf5(f'{dir_path}/ColombiaCountyMapSheet4326.dbf', codec='cp1252')
df_map_sheet = pd.DataFrame(dbf_map_sheet.to_dataframe())
df_map_sheet = df_map_sheet[['MpCodigo', 'PLANCHA']]
df_map_sheet = df_map_sheet.sort_values(by=['PLANCHA'])

# Filetype list
df_county_layer_filetype = pd.read_csv(county_layer_filetype_path, encoding='cp1252', sep=',', dtype={'FileName': 'str', 'EnDesc': 'str', 'EsDesc': 'str'})
#print(df_county_layer_filetype.to_markdown(index=False))

# IGAC - Economic destination
df_county_layer_economic_destination_igac = pd.read_csv(county_layer_economic_destination_igac_path, encoding='cp1252', sep=',', dtype={'FileName': 'str', 'EnDesc': 'str', 'EsDesc': 'str'})
#print(df_county_layer_economic_destination_igac.to_markdown(index=False))
# State list
df_state = df_county['DeCodigo'].unique()


# Main Readme.md
funcs.print_log(file_log, f'<div align="center"><img alt="rcfdtools" src="../../graph/R.GISMobile.svg" width="250px"></div>\n\n')
funcs.print_log(file_log, f'# _{dictionary.dicts['study_name']}_ \n{dictionary.dicts['keywords']}\n\n{dictionary.dicts['study_desc']}\n\n> Check the general [DataSource & ChangeLog](Readme_Datasource.md) Readme file.\n', on_screen=print_on_screen)
funcs.print_log(file_log, f'<img alt="rcfdtools" src="{minimap_link}{country_code}_MiniMapCountry.png" width="600px"></img>', center_div=True, on_screen=print_on_screen)
funcs.print_log(file_log, f'\n## 1. Colombia South America States (es: Departamentos)\n\n{dictionary.dicts['state']}\n', on_screen=print_on_screen)
for state in df_state:
    df_state_info = df_county[df_county['DeCodigo'] == state]
    state_name = df_state_info['DeNombre'].values[0]
    df_county_filter = df_county[df_county['DeCodigo'] == state]
    funcs.print_log(file_log, f'\n* [{state} - {state_name}]({state}.md) ({len(df_county_filter)} Counties)')
funcs.print_log(file_log, f'\n\n\n## 2. File and Field Name Tags\n\n{dictionary.dicts['county_layer_filetype']}\n\n{df_county_layer_filetype.to_markdown(index=False)}\n', on_screen=print_on_screen)
funcs.print_log(file_log, f'\n\n\n## 3. IGAC Property Economic Destination\n\n{dictionary.dicts['county_layer_economic_destination_igac']}\n\n{df_county_layer_economic_destination_igac.to_markdown(index=False)}\n', on_screen=print_on_screen)
funcs.print_log(file_log, f'\n\n#\n\n<div align="center"><img alt="rcfdtools" src="../../graph/qr-code-shp.png" width="250px"><br><sub>Share this research</sub></div><br>', on_screen=print_on_screen)
funcs.print_log(file_log, f'\n\n<sub>{dictionary.dicts['disclaimer']}</sub>', on_screen=print_on_screen)
funcs.print_log(file_log, f'\n\n| [:house: Home](../../../README.md)  | [:beginner: Help / Collab](https://github.com/rcfdtools/R.GISMobile/discussions) |', on_screen=print_on_screen)
funcs.print_log(file_log, f'\n|----------------------------|-------------------------------------------------------------------------------------------|', on_screen=print_on_screen)

# Individual state.md readme files
for state in df_state:
    file_log_name = f'{county_layer_path}/{state}.md'  # Markdown file log
    file_log = open(file_log_name, 'w+', encoding='utf-8')  # w+ create the file if it doesn't exist
    print_dataframe = pd.DataFrame(columns=['MiniMap', 'CountyID', 'CountyName', 'Cadastre', 'MapSheet', 'CountyFiles'])
    df_state_info = df_county[df_county['DeCodigo'] == state]
    state_name = df_state_info['DeNombre'].values[0]
    df_county_filter = df_county[df_county['DeCodigo'] == state]
    funcs.print_log(file_log, f'<div align="center"><img alt="rcfdtools" src="../../graph/R.GISMobile.svg" width="250px"></div>\n\n')
    funcs.print_log(file_log, f'# _{dictionary.dicts['study_name']} for {state} - {state_name} ({len(df_county_filter)} Counties)_ \n{dictionary.dicts['keywords']}\n\n{dictionary.dicts['study_desc']}\n\n> Check the general [DataSource & ChangeLog](Readme_Datasource.md) readme file.<br/>', on_screen=print_on_screen)
    funcs.print_log(file_log, f'> Each _CountyID_ code link contain the [Population and Public Services Demand Projections (PPSD)](https://github.com/rcfdtools/R.HydroTools/blob/main/tool/Population/file/report/Readme.md) report.\n', center_div=False, on_screen=print_on_screen)
    state_latitude = df_state_info['Latitude'].values[0]
    state_longitude = df_state_info['Longitude'].values[0]
    #funcs.print_log(file_log, f'\n# {state} - {state_name} ({len(df_county_filter)} Counties)\n')
    fig_file0a = f'{minimap_link}{country_code}_{state}_MiniMap.png'
    funcs.print_log(file_log, f'<img alt="rcfdtools" src="{fig_file0a}" width="600px"></img>', center_div=True, on_screen=print_on_screen)
    df_county_unique = df_county_filter['MpCodigo'].unique()
    for county in df_county_unique:
        df_cadastre_manager_info = df_cadastre_manager[df_cadastre_manager['mpcodigo'] == county]
        if len(df_cadastre_manager_info) > 0:
            cadastre_manager = df_cadastre_manager_info['Cadastre'].values[0]  ###########
        else:
            cadastre_manager = 'Not found'
        #print(f'County {county}: {cadastre_manager}')
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
        # Map sheets
        map_sheets_filter = df_map_sheet[df_map_sheet['MpCodigo'] == county]
        map_sheets_list = map_sheets_filter['PLANCHA'].unique().tolist()
        map_sheets_txt = ''
        int_separator = 1
        if len(map_sheets_filter) > 0:
            for sheet in map_sheets_list:
                int_separator += 1
                if int_separator <= len(map_sheets_filter) and len(map_sheets_filter) > 1:
                    separator = ','
                else:
                    separator = ''
                map_sheets_txt += f'[{sheet}]({igac_map_sheet_link}{sheet}){separator} '
        else:
            map_sheets_txt = 'Not found'
        print_dataframe.loc[len(print_dataframe)] = [county_minimap, county_ppsd_link, county_name, cadastre_manager, map_sheets_txt, files_txt]
    funcs.print_log(file_log, print_dataframe.to_markdown(index=False), center_div=True)
    funcs.print_log(file_log, f'\n#\n\n<div align="center"><img alt="rcfdtools" src="../../graph/qr-code-shp.png" width="250px"><br><sub>Share this research</sub></div><br>', on_screen = print_on_screen)
    funcs.print_log(file_log, f'\n\n<sub>{dictionary.dicts['disclaimer']}</sub>', on_screen = print_on_screen)
    funcs.print_log(file_log, f'\n\n| [:house: Home](Readme.md)  | [:beginner: Help / Collab](https://github.com/rcfdtools/R.GISMobile/discussions) |', on_screen=print_on_screen)
    funcs.print_log(file_log, f'\n|----------------------------|-------------------------------------------------------------------------------------------|', on_screen=print_on_screen)
