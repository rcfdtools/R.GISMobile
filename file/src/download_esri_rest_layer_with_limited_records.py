1import json
import requests

#service_url = "https://sampleserver6.arcgisonline.com/arcgis/rest/services/Census/MapServer/3/query"
service_url = "https://geodatos.antioquia.gov.co/server/rest/services/Catastro/Visor_Geo/FeatureServer/3"
layer_name_output = 'AntioquiaPredioRural'

all_features = []
offset = 0
record_limit = 1999  # Match or stay below the server's max record count

while True:
    params = {
        "where": "1=1",
        "outFields": "*",
        "returnGeometry": "true",
        "resultOffset": offset,
        "resultRecordCount": record_limit,
        "f": "geojson",
        "verify": "false",
    }

    response = requests.get(service_url, params=params).json()
    features = response.get("features", [])

    if not features:
        break  # Break loop when no more features are returned

    all_features.extend(features)
    offset += len(features)
    print(f"Downloaded {offset} features...")

# Construct final GeoJSON structure
geojson_data = {"type": "FeatureCollection", "features": all_features}

with open("large_dataset.geojson", "w") as f:
    json.dump(geojson_data, f)