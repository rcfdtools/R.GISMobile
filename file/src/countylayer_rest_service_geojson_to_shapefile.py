# https://github.com/rcfdtools
# Download ESRI Rest Service as geojson and convert to shapefile (GeoPandas)

# First: download layers in geojson format from Python console
# pip install esridump
# From CMD as administrator run
# esri2geojson https://geodatos.antioquia.gov.co/server/rest/services/Catastro/Visor_Geo/FeatureServer/0 AntioquiaLimiteMunicipal202608.geojson
# esri2geojson https://geodatos.antioquia.gov.co/server/rest/services/Catastro/Visor_Geo/FeatureServer/1 AntioquiaVereda202608.geojson
# esri2geojson https://geodatos.antioquia.gov.co/server/rest/services/Catastro/Visor_Geo/FeatureServer/2 AntioquiaCorreguimiento202608.geojson
# esri2geojson https://geodatos.antioquia.gov.co/server/rest/services/Catastro/Visor_Geo/FeatureServer/3 AntioquiaPredioRural202608.geojson
# esri2geojson https://geodatos.antioquia.gov.co/server/rest/services/Catastro/Visor_Geo/FeatureServer/4 AntioquiaContruccionRural202608.geojson
# esri2geojson https://geodatos.antioquia.gov.co/server/rest/services/Catastro/Visor_Geo/FeatureServer/5 AntioquiaBarrios202608.geojson
# esri2geojson https://geodatos.antioquia.gov.co/server/rest/services/Catastro/Visor_Geo/FeatureServer/6 AntioquiaPredioUrbano202608.geojson
# esri2geojson https://geodatos.antioquia.gov.co/server/rest/services/Catastro/Visor_Geo/FeatureServer/7 AntioquiaContruccionUrbano202608.geojson
# esri2geojson https://services2.arcgis.com/RVvWzU3lgJISqdke/ArcGIS/rest/services/Base_Catastral_Publica_del_Gestor_IGAC_06_2026/FeatureServer/17 igac_202606_registro1.geojson
# esri2geojson https://services2.arcgis.com/RVvWzU3lgJISqdke/ArcGIS/rest/services/Base_Catastral_Publica_del_Gestor_IGAC_06_2026/FeatureServer/18 igac_202606_registro2.geojson
# esri2geojson https://www.medellin.gov.co/servidormapas/rest/services/ServiciosCatastro/Base_Catastral/MapServer/3 MedellinLote202608.geojson
# esri2geojson https://www.medellin.gov.co/servidormapas/rest/services/ServiciosCatastro/Base_Catastral/MapServer/5 MedellinConstruccion202608.geojson
# esri2geojson https://portalidem.metropol.gov.co/server/rest/services/Barbosa_Catastro/MapServer/7 05079BarbosaPredioUbano202608.geojson
# esri2geojson https://portalidem.metropol.gov.co/server/rest/services/Barbosa_Catastro/MapServer/8 05079BarbosaPredioRural202608.geojson
# esri2geojson https://portalidem.metropol.gov.co/server/rest/services/Barbosa_Catastro/MapServer/5 05079BarbosaConstruccionUbana202608.geojson
# esri2geojson https://portalidem.metropol.gov.co/server/rest/services/Barbosa_Catastro/MapServer/6 05079BarbosaConstruccionRural202608.geojson

# Convert geojson to shapefile (GeoPandas)
import geopandas as gpd

file_name_input = '05631SabanetaPredioUrbano202608'
#file_name_output = '05631_Rural_Building_202608'
#file_name_output = '05631_Urban_Building_202608'
#file_name_output = '05631_Rural_Lot_202608'
file_name_output = '05631_Urban_Lot_202608'

# 1. Read the GeoJSON file into a GeoDataFrame
gdf = gpd.read_file(f'../geojson/{file_name_input}.geojson')

# 2. Write the GeoDataFrame out as an ESRI Shapefile
gdf.to_file(f'../temp/{file_name_output}.shp', driver="ESRI Shapefile")


# Batch Converting Multiple Files (GeoPandas)
'''
import glob
import geopandas as gpd

# Find all geojson files in the directory
for file in glob.glob("path/to/folder/*.geojson"):
    gdf = gpd.read_file(file)
    output_name = file.replace(".geojson", ".shp")
    gdf.to_file(output_name, driver="ESRI Shapefile")
'''
