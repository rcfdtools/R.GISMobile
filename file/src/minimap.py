# https://github.com/rcfdtools
# -*- coding: UTF-8 -*-
# MiniMAP

# Libraries
import functions as funcs
from simpledbf import Dbf5
import tabulate
import matplotlib.pyplot as plt
import pandas as pd
pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# General parameters
minimap_path = '../gis/GISMobile_MiniMAP/'
run_colombia_state = True

# Colombia State MiniMAP
# Source:
if run_colombia_state:
    country_code = '57'
    dbf_colombia_state = Dbf5('../shp/ColombiaState4326.dbf', codec='cp1252')
    df_colombia_state = pd.DataFrame(dbf_colombia_state.to_dataframe())
    df_colombia_state = df_colombia_state[['DeCodigo', 'DeNombre', 'DeNorma', 'Latitude', 'Longitude']]
    df_colombia_state = df_colombia_state.sort_values(by=['DeCodigo', 'DeNombre'])
    df_colombia_state.drop(df_colombia_state[df_colombia_state['DeCodigo'] == '00'].index, inplace=True)
    db_colombia_state_list = df_colombia_state['DeCodigo'].unique()
    print(f'Colombia State: {db_colombia_state_list}\n')
    for minimap_name in db_colombia_state_list:
        figure = f'{minimap_path}{country_code}_{minimap_name}_LocationMap.png'
        df_state_info = df_colombia_state[df_colombia_state['DeCodigo'] == minimap_name]
        state_name = df_state_info['DeNombre'].values[0]
        state_latitude = df_state_info['Latitude'].values[0]
        state_longitude = df_state_info['Longitude'].values[0]
        print(figure)
        location_map_plot = funcs.location_map(point_latitude = state_latitude, point_longitude = state_longitude, point_name = state_name.upper(), state_filter = minimap_name, county_label_on = True)
        location_map_plot.savefig(figure, dpi=120)
        plt.close()



# Colombia County MiniMAP
# Source:
dbf_colombia_county = Dbf5('../shp/ColombiaCounty4326.dbf', codec='cp1252')
df_colombia_county = pd.DataFrame(dbf_colombia_county.to_dataframe())
df_colombia_county = df_colombia_county[['DeCodigo', 'DeNombre', 'MpCodigo', 'MpNombre', 'MpNorma', 'Latitude', 'Longitude']]
df_colombia_county = df_colombia_county.sort_values(by=['DeCodigo', 'DeNombre', 'MpNombre', 'MpCodigo'])
df_colombia_county.drop(df_colombia_county[df_colombia_county['MpCodigo'] == '00000'].index, inplace=True)