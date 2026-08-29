import json
import requests

# 1. Define the REST Service URL down to the specific layer ID (e.g., /0)
# Append '/query' to the end of the layer URL
#service_url = "https://sampleserver6.arcgisonline.com/arcgis/rest/services/Census/MapServer/3/query"
service_url = "https://geodatos.antioquia.gov.co/server/rest/services/Catastro/Visor_Geo/FeatureServer/3"
layer_name_output = 'AntioquiaPredioRural'

# 2. Set up parameters to request all fields and geometries
params = {
    "where": "1=1",  # Grabs all records
    "outFields": "*",  # Grabs all columns
    "returnGeometry": "true",
    "f": "geojson",  # Output format (use 'json' for Esri JSON format)
}

# 3. Send the request
print("Downloading data...")
response = requests.get(service_url, params=params)

# 4. Check response status and save to a local file
if response.status_code == 200:
    data = response.json()

    # Save to a local GeoJSON file
    output_file = f"{layer_name_output}.geojson"
    with open(output_file, "w") as f:
        json.dump(data, f, indent=4)

    print(f"Success! Data saved to {output_file}")
else:
    print(f"Failed to download. Status code: {response.status_code}")