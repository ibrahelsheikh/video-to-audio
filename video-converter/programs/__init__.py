# unzip file

import os
import zipfile

def unzip_file(zip_file, unzip_dir):
    if not os.path.exists(unzip_dir):
        os.makedirs(unzip_dir)
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(unzip_dir)

# rename folder in python
def rename_folder (file):
    pass

unzip_file('ffmpeg.zip' ,os.path.abspath(os.getcwd()))
