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
minimap_path = '../gis/MiniMAP/'
dpi_resolution = 180
run_colombia_state = False
run_colombia_county_national_point = False

# Colombia State MiniMAP
# Source:
if run_colombia_state:
    dpi_resolution = 180
    country_code = '57'
    dbf_layer = Dbf5('../shp/ColombiaState4326.dbf', codec='cp1252')
    df_layer = pd.DataFrame(dbf_layer.to_dataframe())
    df_layer = df_layer[['DeCodigo', 'DeNombre', 'DeNorma', 'Latitude', 'Longitude']]
    df_layer = df_layer.sort_values(by=['DeCodigo', 'DeNombre'])
    df_layer.drop(df_layer[df_layer['DeCodigo'] == '00'].index, inplace=True)
    db_layer_list = df_layer['DeCodigo'].unique()
    print(f'Colombia State: {db_layer_list}\n')
    for minimap_name in db_layer_list:
        figure = f'{minimap_path}{country_code}_{minimap_name}_LocationMap.png'
        df_state_info = df_layer[df_layer['DeCodigo'] == minimap_name]
        name = df_state_info['DeNombre'].values[0]
        latitude = df_state_info['Latitude'].values[0]
        longitude = df_state_info['Longitude'].values[0]
        print(figure)
        location_map_plot = funcs.location_map(point_latitude = latitude, point_longitude = longitude, point_name = f'{minimap_name} - {name.upper()}', state_filter = minimap_name, county_label_on = True, show_marker = False, horizontal_size = 6, vertical_size = 6)
        location_map_plot.savefig(figure, dpi=dpi_resolution)
        plt.close()

# Colombia County National Point Location
# Source:
if run_colombia_county_national_point:
    dpi_resolution = 180
    country_code = '57'
    dbf_layer = Dbf5('../shp/ColombiaCounty4326.dbf', codec='cp1252')
    df_layer = pd.DataFrame(dbf_layer.to_dataframe())
    df_layer = df_layer[['MpCodigo', 'MpNombre', 'MpNorma', 'Latitude', 'Longitude']]
    df_layer = df_layer.sort_values(by=['MpCodigo', 'MpNombre'])
    df_layer.drop(df_layer[df_layer['MpCodigo'] == '00000'].index, inplace=True)
    db_layer_list = df_layer['MpCodigo'].unique()
    print(f'Colombia county: {db_layer_list}\n')
    for minimap_name in db_layer_list:
        figure = f'{minimap_path}{country_code}_{minimap_name}_LocationMapCountry.png'
        df_state_info = df_layer[df_layer['MpCodigo'] == minimap_name]
        name = df_state_info['MpNombre'].values[0]
        latitude = df_state_info['Latitude'].values[0]
        longitude = df_state_info['Longitude'].values[0]
        print(figure)
        location_map_plot = funcs.location_map(point_latitude = latitude, point_longitude = longitude, point_name = f'{minimap_name} - {name.upper()}', state_filter = 'All', county_label_on = True, show_marker = True, horizontal_size = 6, vertical_size = 6)
        location_map_plot.savefig(figure, dpi=dpi_resolution)
        plt.close()