# https://github.com/rcfdtools/R.GISMobile/blob/main/README.md
# Compress county files into a group ZIP file by CountyID

import os
import glob
import zipfile
from pathlib import Path

directory = '../shp/'
run_complete = False # ● Run for each county founded. Use False if you want to get the unique value list
version_info = f'# Dataset Information\n\n* More information in https://github.com/rcfdtools/R.GISMobile/blob/main/file/shp/Readme.md'
files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
exclude_file_type = ['.zip', '.xml', '.cpg', '.sbn', '.sbx', '.qix', '.qmd', '.ovr']
files = [item for item in files if not any(exclude in item for exclude in exclude_file_type)]
#print(files)
target_slice_character = '_'
county_list = [item.split(target_slice_character)[0] for item in files]
target_slice_character = '.'
county_list = [item.split(target_slice_character)[0] for item in county_list]
county_list = list(set(county_list))
county_list = sorted(county_list)
print(county_list)
if run_complete:
    for county in county_list:
        readme_path = f'{directory}{county}_Readme.md'
        # Create a version file
        with open(readme_path, 'w', encoding='utf-8') as file:
            file.write(version_info)
        filtered = [x for x in files if county in x]
        if not os.path.exists(readme_path):
            filtered.append(f'{county}_Readme.md')
        print(f'Compressing: {filtered}')
        '''
        with zipfile.ZipFile(f'{directory}/{county}.zip', mode='w') as archive:
            for file in filtered:
                archive.write(f'{directory}/{file}', compress_type=zipfile.ZIP_DEFLATED) # compress_type=zipfile.ZIP_DEFLATED actually shrinks the file size
        '''