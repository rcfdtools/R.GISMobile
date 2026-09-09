# https://github.com/rcfdtools
# IGAC Record 1 and Record 2
# https://www.igac.gov.co/index.php/node/31261: Record 1, Record 2 and cadastral data.
# Record 1 >> https://www.arcgis.com/sharing/rest/content/items/fd52b3ff0ca84c3f91aa698c4b0125f0/data
# Record 2 >> https://www.arcgis.com/sharing/rest/content/items/12c1d317721a41629301d720ad0ed1e2/data

# Libraries
import glob
import pandas as pd
from pathlib import Path

# General parameters
version_file = '202607' # ● The yyyymm version dataset from IGAC
output_path = '../temp/' # ●
run_csv_join = False # ● Run the csv join
run_csv_county_segmentation = True # ● Run the csv join

# Processing R1 join .csv files
input_path = '../table/REGISTRO_R1/' # ● Folder source with independent .csv files
join_csv_file_name = f'R1_{version_file}.csv' # ● Joined csv name
if run_csv_join:
    csv_files = glob.glob(f'{input_path}*.csv')
    print(f'R2 (csv files to join): {csv_files}')
    df_list = [pd.read_csv(file, encoding='latin-1', dtype={'DEPARTAMENTO': str, 'MUNICIPIO': str, 'NUMERO_PREDIAL': str, 'DIRECCION': str, 'DESTINO_ECONOMICO': str, 'NUMERO_PREDIAL_ANTERIOR': str}) for file in csv_files]
    combined_df = pd.concat(df_list, ignore_index=True)
    combined_df.to_csv(f'{output_path}{join_csv_file_name}', index=False)
    del combined_df

# Processing R2 join .csv files
input_path = '../table/REGISTRO_R2/' # ● Folder source with independent .csv files
join_csv_file_name = f'R2_{version_file}.csv' # ● Joined csv name
if run_csv_join:
    csv_files = glob.glob(f'{input_path}*.csv')
    print(f'R2 (csv files to join): {csv_files}')
    df_list = [pd.read_csv(file, encoding='latin-1', dtype={'DEPARTAMENTO': str, 'MUNICIPIO': str, 'NUMERO_PREDIAL': str, 'DIRECCION': str, 'DESTINO_ECONOMICO': str, 'NUMERO_PREDIAL_ANTERIOR': str, 'ZONA_FISICA_1': str, 'ZONA_FISICA_2': str}) for file in csv_files]
    combined_df = pd.concat(df_list, ignore_index=True)
    combined_df.to_csv(f'{output_path}{join_csv_file_name}', index=False)
    del combined_df

# Split R1 into county .csv files
if run_csv_county_segmentation:
    df = pd.read_csv(f'{output_path}R1_{version_file}.csv', encoding='latin-1', dtype={'DEPARTAMENTO': str, 'MUNICIPIO': str, 'NUMERO_PREDIAL': str, 'DIRECCION': str, 'DESTINO_ECONOMICO': str, 'NUMERO_PREDIAL_ANTERIOR': str})
    counties = df['MUNICIPIO'].unique().tolist()
    counties = sorted(counties)
    print(f'R1 ({len(counties)} counties found to split): {counties}')
    for county in counties:
        filename = Path(f'{output_path}{county}_R1_{version_file}.csv')
        if not filename.is_file():
            filtered_df = df[df['MUNICIPIO'] == county]
            filtered_df.to_csv(filename, index=False)
            print(f'County {county}: {len(filtered_df)} records ({filename})')
            del filtered_df

# Split R2 into county .csv files
if run_csv_county_segmentation:
    df = pd.read_csv(f'{output_path}R2_{version_file}.csv', encoding='latin-1', dtype={'DEPARTAMENTO': str, 'MUNICIPIO': str, 'NUMERO_PREDIAL': str, 'DIRECCION': str, 'DESTINO_ECONOMICO': str, 'NUMERO_PREDIAL_ANTERIOR': str, 'ZONA_FISICA_1': str, 'ZONA_FISICA_2': str})
    counties = df['MUNICIPIO'].unique().tolist()
    counties = sorted(counties)
    print(f'R2 ({len(counties)} counties found to split): {counties}')
    for county in counties:
        filename = Path(f'{output_path}{county}_R2_{version_file}.csv')
        if not filename.is_file():
            filtered_df = df[df['MUNICIPIO'] == county]
            filtered_df.to_csv(filename, index=False)
            print(f'County {county}: {len(filtered_df)} records ({filename})')
            del filtered_df