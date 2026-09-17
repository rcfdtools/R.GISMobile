# https://github.com/rcfdtools/R.GISMobile/blob/main/README.md
# Download massive files from CountyLayer
# Requires a file with the required counties list, e.g., /file/table/CountyLayerList.txt

# Libraries
import os
from urllib.parse import urlparse
from pathlib import Path
import requests
import pandas as pd
import tabulate

# General parameters
county_list_to_download = 'C:/Temp/countylayer_download_list.txt' # ● File with the list of the required county codes to download, must have the header CountyID
output_path = 'C:/Temp/CountyLayer/' # './CountyLayer/' # ● Your local path to save the download files
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
    print(f'Getting CountyLayer file index: {url}')
    df_files = pd.read_csv(f'{output_path}{county_layer_file_index}', dtype={'CountyID': 'str'})
else:
    print(f"Failed to download file. Status code: {response.status_code}")

# General procedure
df = pd.read_csv(county_list_to_download, dtype={'CountyID': 'str'})
county_list = df['CountyID'].to_list()
print(f'\nCounties to download: {county_list}\n')
df_files_filtered = df_files[df_files['CountyID'].isin(county_list)]
df_files_filtered['url'] = main_url + df_files_filtered['FilePath'] + '/' + df_files_filtered['Filename']
print(f'Files to download\n\n{df_files_filtered.to_markdown(index=False)}')
files = df_files_filtered['url'].to_list()
print('\nStarting downloading files\n')
for url in files:
    filename = os.path.basename(urlparse(url).path)
    path_filename = f'{output_path}{filename}'
    if Path(path_filename).is_file():
        print(f'* Already downloaded {url}')
    else:
        response = requests.get(url)
        if response.status_code == 200:
            # Open a local file in 'write binary' (wb) mode
            with open(path_filename, "wb") as file:
                file.write(response.content)
            print(f'* Downloading {url}')
        else:
            print(f'Failed to download file {url}. Status code: {response.status_code}')
print('\nDownload completed')