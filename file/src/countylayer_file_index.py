# https://github.com/rcfdtools/R.GISMobile/blob/main/README.md
# Creates a file index with all the compressed files contained in /shp
# The file/table/countylayer_file_index.csv is used to automate the downloads from the CountyLayer repository

# Libraries
from pathlib import Path
import countylayer_functions as funcs
import pandas as pd

# General parameters
directory_path = Path('../shp/')
extensions = {'.zip', '.rar', '.7z'}
columns = ['CountyID', 'FilePath', 'Filename', 'SizeMB']
df = pd.DataFrame(columns=columns)

# Procedure
found_files = [
    file for file in directory_path.rglob('*') 
    if file.is_file() and file.suffix.lower() in extensions
]

# Save index file
for f in found_files:
    size_mb = f.stat().st_size / (1024 * 1024)
    file_folder = str(f.parent)
    file_folder = file_folder.replace('..', '')
    print(f'{f.name.split('_')[0]},{file_folder},{f.name},{round(size_mb, 2)}')
    df.loc[len(df)] = [f.name.split('_')[0],file_folder,f.name,round(size_mb, 2)]
df.to_csv('../table/countylayer_file_index.csv', index=False)
