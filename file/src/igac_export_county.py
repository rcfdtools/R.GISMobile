# https://github.com/rcfdtools/R.GISMobile/blob/main/README.md
# Export counties to individual shapefile from the global IGAC geopackage or a global layer using QGIS (Tested in QGIS version 4.0.1)
# Select a layer in the QGIS Layer Panel

import os
from qgis.core import QgsProject, QgsVectorFileWriter, QgsCoordinateTransformContext
import processing

# Export layers
output_path = 'D:/R.GISMobile/file/temp/'
layer = iface.activeLayer()
layer_suffix = '_Rural_Lot_202608' # ● Suffix for label each exported layer, e.g., U_TERRENO correspond to 'Urban'
index_field = 'CountyID' # ● Index field in the selected layer
print_explicit = False # ● Show explicit running in console
run_complete = True # ● Run for each index_field value. Use False if you want to get the unique value list
load_layer_in_map = False # ● Load each exported layer into the current project map
crs_target_code = '9377'
crs_target = QgsCoordinateReferenceSystem(f'EPSG:{crs_target_code}')
idx = layer.fields().indexOf(index_field)
values = sorted(layer.uniqueValues(idx))
print(f'Type: {type(values)}\n{values}')
if run_complete:
    for i in values:
        path = f'{output_path}{i}{layer_suffix}.shp'
        layer_filter = f'"{index_field}" = \'{i}\'' # Note: Use double quotes for fields, single quotes for text values
        if print_explicit:
            print(f'Processing: {path}')
            print(f'Filter: {layer_filter}')
        layer.setSubsetString("")
        layer.setSubsetString(layer_filter)
        parameters = {
            'INPUT': layer,
            'OUTPUT': path,
            'TARGET_CRS': crs_target,
            'LAYER_NAME': f'{i}{layer_suffix}'
        }    
        #result = processing.run("native:savefeatures", parameters)
        result = processing.run("native:reprojectlayer", parameters)
        if load_layer_in_map: new_layer = iface.addVectorLayer(path, f'{i}_{layer_suffix}', "ogr")
    

