# -*- coding: UTF-8 -*-

import os
import glob
import pandas as pd
import geopandas
from exif import Image
from pathlib import *
import tabulate  # required for print tables in Markdown using pandas

def decimal_coords(coords, ref):
 decimal_degrees = coords[0] + coords[1] / 60 + coords[2] / 3600
 if ref == 'S' or ref == 'W':
     decimal_degrees = -decimal_degrees
 return decimal_degrees

def image_coordinates(img_path):
    with open(img_path, 'rb') as src:
        img = Image(src)
    if img.has_exif:
        try:
            img.gps_longitude
            coords = (decimal_coords(img.gps_latitude,
                      img.gps_latitude_ref),
                      decimal_coords(img.gps_longitude,
                      img.gps_longitude_ref),
                      img.gps_altitude)
        except AttributeError:
            print('No Coordinates')
    else:
        print('The Image has no EXIF information')
    print(f"Image {src.name}, OS Version:{img.get('software', 'Not Known')} ------")
    print(f"Was taken: {img.datetime_original}, and has coordinates:{coords}")

def image_info(img_path):
    coords = ''
    with open(img_path, 'rb') as src:
        img = Image(src)
    if img.has_exif:
        try:
            img.gps_longitude
            coords = (decimal_coords(img.gps_latitude,
                      img.gps_latitude_ref),
                      decimal_coords(img.gps_longitude,
                      img.gps_longitude_ref),
                      img.gps_altitude)
            cx = decimal_coords(img.gps_longitude, img.gps_longitude_ref)
            cy = decimal_coords(img.gps_latitude, img.gps_latitude_ref)
        except AttributeError:
            print('No Coordinates')
    else:
        print('The Image has no EXIF information')
    info = f"**File: {src.name}**. OS version: {img.get('software', 'Not Known')}. Date: {img.datetime_original}"
    print(info)
    readme_file.write(info+'\n')
    if coords:
        map_location = ('Location over [Google Maps](http://maps.google.com/maps?q=' + str(
            cy) + ',' + str(cx) + ') or [Openstreet Map](https://www.openstreetmap.org/query?lat=' + str(cy) + '&lon=' + str(cx) + ')')
        print(f"Coordinates:{coords}")
        readme_file.write(f"<br>Coordinates & altitude: {coords}<br>")
        readme_file.write(map_location + '\n')

# Variables
path = 'D:/R.GISPython/GISMobile/.poi/'
path_www = 'https://github.com/rcfdtools/R.GISPython/tree/main/GISMobile/.poi/'
poi_file = 'poi.csv'
geojson_file = 'Readme.md'
poi_cols = ['POI', 'Latitude', 'Longitude', 'Altitude', 'Date', 'Name', 'Credit', 'Category', 'Link']
exclude_folder = ['.shp', '.temp']
picture_format = ['.jpg', '.png', '.tif']
directories = [d for d in os.listdir(os.getcwd()) if os.path.isdir(d)]

# Processing directories
if os.path.isfile(path+poi_file):
    os.remove(path+poi_file)
df = pd.DataFrame()
print('Directories:', directories)
for i in directories:
    if i not in exclude_folder:
        readme_file = open(path+i+'/'+'Readme.md', 'w+')   # w+ create the file if it doesn't exist
        poi_path = path+i+'/'+poi_file
        print('Processing: %s' %poi_path)
        df1 = pd.read_csv(poi_path)  # Esri shapefile does not support datetime fields with parse_dates=['Date']
        readme_file.write('## %s (%s)\nCréditos: %s<br>Categoría: %s\n\n' %(str(df1['Name'][0]), str(df1['Date'][0]), str(df1['Credit'][0]), str(df1['Category'][0])))
        geojson = '```geojson\n{\n  "type": "Feature",\n  "geometry": {\n    "type": "Point", \n    "coordinates": ['+str(df1['Longitude'][0])+', '+str(df1['Latitude'][0])+']\n  }, \n  "properties": {\n    "Name": "'+df1['Name'][0]+'"\n  }\n}\n```\n\n'
        readme_file.write(geojson)
        df1['POI'] = i
        df1['Link'] = path_www+i+'/Readme.md'
        df = pd.concat([df, df1], ignore_index=True)
        picture_path = path+i+'/'
        picture_files = [x for x in Path(picture_path).iterdir() if x.is_file()]
        for picture in picture_files:
            picture_ext = os.path.splitext(picture)
            if picture_ext[1] in picture_format:
                filename_absolute = os.path.basename(picture)
                print(filename_absolute)
                image_info(i+'/'+filename_absolute)
                readme_file.write('![GISMobile.POI]('+filename_absolute+')\n\n')
        readme_file.write('| [:house: Inicio](../Readme.md) |\n|---|')
df = df[poi_cols]  # Reordering cols
print(df)
df.to_csv(path+poi_file, encoding='utf-8', index=False)

# Create POI shapefile
gdf = geopandas.GeoDataFrame(df)
gdf.set_geometry(
    geopandas.points_from_xy(gdf['Longitude'], gdf['Latitude']),
    inplace=True, crs='EPSG:4326')
gdf.drop(['Latitude', 'Longitude'], axis=1, inplace=True)  # optional
gdf.to_file('.shp/poi.shp')

# Create POI geoJSON
if os.path.isfile(path+geojson_file):
    os.remove(path+geojson_file)
geojson_file_write = open(path+geojson_file, 'w+')   # w+ create the file if it doesn't exist
df = pd.read_csv(path+poi_file)
geojson_file_write.write('## Puntos de interés - POI\n\n### Mapa localización de puntos de interés en GISMobile\n\n')
geojson_file_write.write('```topojson\n{"type": "Topology", "objects": {"example": {"type": "GeometryCollection","geometries": [\n')
print('Records: %i' %len(df))
for i in range(0,len(df)):
    if df.loc[i]['Longitude'] and df.loc[i]['Latitude']:
        properties = ('"POI": "%s", "Category": "%s", "Name": "%s", "Date": "%s", "Credits": "%s", "URL": "%s"'
                      %(str(df.loc[i]['POI']),
                        str(df.loc[i]['Category']),
                        str(df.loc[i]['Name']),
                        str(df.loc[i]['Date']),
                        str(df.loc[i]['Credit']),
                        str(df.loc[i]['Link'])))
        geojson_file_write.write('{"type": "Point","properties": {'+properties+'},"coordinates": ['+str(df.loc[i]['Longitude'])+','+str(df.loc[i]['Latitude'])+']}')
        if i <= len(df)-2:
            geojson_file_write.write(',\n')
        else:
            geojson_file_write.write('\n')
geojson_file_write.write(']}}}\n\n```')
geojson_file_write.write('\n\n### Estadísticas generales por categoría\n\n')
df2 = df.groupby(['Category'])['POI'].agg('count').reset_index()
df2.index.name = '#'
geojson_file_write.write(df2.to_markdown(index=False))
geojson_file_write.write('\n\n\n### Estadísticas generales por autor\n\n')
df2 = df.groupby(['Credit'])['POI'].agg('count').reset_index()
df2.index.name = '#'
geojson_file_write.write(df2.to_markdown(index=False))
geojson_file_write.write('\n\n\n### POI list\n\n')
df.index.name = '#'
geojson_file_write.write(df.to_markdown(index=False))

# https://medium.com/spatial-data-science/how-to-extract-gps-coordinates-from-images-in-python-e66e542af354
# https://stackoverflow.com/questions/141291/how-to-list-only-top-level-directories-in-python
# https://stackoverflow.com/questions/14176166/list-only-files-in-a-directory
# https://stackoverflow.com/questions/7336096/python-glob-without-the-whole-path-only-the-filename
# https://www.geeksforgeeks.org/python-list-files-in-a-directory/
# https://gis.stackexchange.com/questions/147156/making-shapefile-from-pandas-dataframe
# https://python-geojson.readthedocs.io/en/latest/#geometrycollection
# https://zulko.github.io/moviepy/