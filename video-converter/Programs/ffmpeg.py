# unzip file

from os import makedirs
from pathlib import Path
from shutil import rmtree
from zipfile import ZipFile


def unzip_file(zip_filepath: Path, unzip_dir: Path):
    if unzip_dir.exists():
        rmtree(unzip_dir)
    else:
        makedirs(unzip_dir)
        
    with ZipFile(zip_filepath, 'r') as zip_file:
        zip_file.extractall(unzip_dir)

def unzip_ffmpeg():
    ffmpeg_zip_filepath = Path(__file__).parent / "ffmpeg.zip"
    unzip_dir = Path(__file__).parent / "ffmpeg"
    unzip_file(ffmpeg_zip_filepath, unzip_dir)