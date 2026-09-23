import pandas as pd

# Create poi_picture.shp & poi_picture.geojson
df = pd.read_csv('D:/R.GISMobile/file/gis/POI/poi_picture.csv')
print(f'Initial: {len(df)} pictures')
df = df[~((df['Longitude'] == 0) & (df['Latitude'] == 0))]
print(f'Cleaned: {len(df)} pictures with coordinates')