# https://github.com/rcfdtools/R.GISMobile/blob/main/README.md
# Compress county files into individual ZIP files

import os
import glob
import zipfile
from pathlib import Path

directory = '../shp/'
run_complete = True # ● Run for each county founded. Use False if you want to get the unique value list
version_info = f'# Dataset Information\n\n* More information in https://github.com/rcfdtools/R.GISMobile/blob/main/file/shp/Readme.md'
files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
exclude_file_type = ['.zip', '.xml', '.cpg', '.sbn', '.sbx', '.qix', '.qmd', '.ovr']
files = [item for item in files if not any(exclude in item for exclude in exclude_file_type)]
#print(f'Files founded: {files}')
files_individual = [f.stem for f in Path(directory).iterdir() if f.is_file()]
exclude_files = {'Readme', 'R.GISMobile'}
files_individual = [item for item in files_individual if item not in exclude_files]
files_individual = [item for item in files_individual if not any(exclude in item for exclude in exclude_file_type)]
files_individual = list(set(files_individual))
files_individual = sorted(files_individual)
#print(f'Files individual: {files_individual}\n')
print(f'Compressing {len(files)} files into {len(files_individual)} zip files in {directory}')
if run_complete:
    for county_file in files_individual:
        filtered = [x for x in files if county_file in x]
        #print(f'Compressing {county_file}.zip: {filtered}')
        # Create a zip file
        zip_path = Path(f'{directory}/{county_file}.zip')
        if not zip_path.is_file():
            print(f'Compressing {county_file}.zip')
            with zipfile.ZipFile(f'{directory}/{county_file}.zip', mode='w') as archive:
                for file in filtered:
                    #archive.write(f'{directory}/{file}', compress_type=zipfile.ZIP_DEFLATED) # compress_type=zipfile.ZIP_DEFLATED actually shrinks the file size
                    archive.write(f'{directory}/{file}', compress_type=zipfile.ZIP_DEFLATED) # compress_type=zipfile.ZIP_DEFLATED actually shrinks the file size
        else:
            print(f'File {county_file}.zip already exists')
print(f'\nProcess completed.')