# Google prompt: geojson table to .csv python

import geopandas as gpd

# 1. Load the GeoJSON file into a GeoDataFrame
#gdf = gpd.read_file('../geojson/igac_202606_registro1_sample.geojson')

'''
# 2. (Optional) Convert the geometry column to WKT format so Excel/GIS can read it
# If you don't do this, the raw geometry object will just write as a string
gdf['geometry'] = gdf['geometry'].apply(lambda x: x.wkt if x else None)
'''

# 3. Save to a CSV file
#gdf.to_csv('../geojson/output.csv', index=False)

# With JSON

import json
import pandas as pd

# 1. Load the raw GeoJSON data
with open('../geojson/igac_202606_registro1_sample.geojson', 'r', encoding='utf-8') as f:
    geojson_data = json.load(f)

# 2. Flatten the 'properties' list from the features array
df = pd.json_normalize(geojson_data['features'])

# 3. Clean up column names (removes the 'properties.' prefix)
df.columns = [col.replace('properties.', '') for col in df.columns]

# 4. (Optional) Drop geometry tracking columns if they were pulled in
df = df.drop(columns=[col for col in df.columns if 'geometry' in col], errors='ignore')

# 5. Export to CSV
df.to_csv('../geojson/output.csv', index=False)