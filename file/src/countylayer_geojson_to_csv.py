# Google prompt: geojson table to .csv python

import json
import pandas as pd

# Libraries
input_path = '../geojson/'
output_path = '../geojson/'
file_name = 'IDEAM_SERIESTIEMPOESTACIONES_VIEWZZZZ'

# With JSON
with open(f'{input_path}{file_name}.geojson', 'r', encoding='utf-8') as f:
    geojson_data = json.load(f)
df = pd.json_normalize(geojson_data['features'])
df.columns = [col.replace('properties.', '') for col in df.columns]
df = df.drop(columns=[col for col in df.columns if 'geometry' in col], errors='ignore')
print(f'Dataset {file_name}.geojson with {len(df)} records')
df.to_csv(f'{input_path}{file_name}.csv', index=False)
del df

