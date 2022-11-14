# unzip file

from os import makedirs
from pathlib import Path
from shutil import rmtree
from zipfile import ZipFile


def unzip_file(zip_filepath: Path, unzip_dir: Path, current_dir: Path):
    if unzip_dir.exists() == False:
        with ZipFile(zip_filepath, 'r') as zip_file:
            zip_file.extractall(current_dir)


def unzip_ffmpeg():
    ffmpeg_zip_filepath = Path(__file__).parent / "ffmpeg.zip"
    unzip_dir = Path(__file__).parent / "ffmpeg"
    current_dir = Path(__file__).parent
    unzip_file(ffmpeg_zip_filepath, unzip_dir, current_dir)


def get_ffmpeg_path():
    return Path(__file__).parent / "ffmpeg" / "bin"
