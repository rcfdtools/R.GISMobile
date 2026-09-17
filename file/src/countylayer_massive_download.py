# https://github.com/rcfdtools/R.GISMobile/blob/main/README.md

# Libraries
from pathlib import Path
import requests
import pandas as pd
import tabulate

# General parameters
county_list_to_download = 'C:/Temp/CountyLayerList.txt' # File with the list of the required county codes to download, must have the header CountyID
output_path = 'C:/Temp/CountyLayer/' # './CountyLayer/'
Path(output_path).mkdir(parents=True, exist_ok=True)
main_url = 'https://github.com/rcfdtools/R.GISMobile/raw/refs/heads/main/file'
county_layer_file_index = 'countylayer_file_index.csv'

# Download countylayer_file_index.csv (table with all the available files in CountyLayer)
url = 'https://github.com/rcfdtools/R.GISMobile/raw/refs/heads/main/file/table/countylayer_file_index.csv'
response = requests.get(url)
if response.status_code == 200:
    # Open a local file in 'write binary' (wb) mode
    with open(f'{output_path}{county_layer_file_index}', "wb") as file:
        file.write(response.content)
    print(f'* Downloading {url}')
    df_files = pd.read_csv(f'{output_path}{county_layer_file_index}', dtype={'CountyID': 'str'})
else:
    print(f"Failed to download file. Status code: {response.status_code}")


# General procedure
df = pd.read_csv(county_list_to_download, dtype={'CountyID': 'str'})
county_list = df['CountyID'].to_list()
print(county_list)
df_files_filtered = df_files[df_files['CountyID'].isin(county_list)]
#df_files_filtered['url'] = f'{main_url}{df_files_filtered['FilePath']}/{df_files_filtered['Filename']}'
df_files_filtered['url'] = main_url + df_files_filtered['FilePath'] + '/' + df_files_filtered['Filename']
print(df_files_filtered.to_markdown(index=False))

files = df_files_filtered['url'].to_list()
print(files)

for i in files:
    url = i
    response = requests.get(url)
    if response.status_code == 200:
        # Open a local file in 'write binary' (wb) mode
        with open(f'{output_path}{i}', "wb") as file:
            file.write(response.content)
        print(f'* Downloading {url}')
    else:
        print(f'Failed to download file {i}. Status code: {response.status_code}')
