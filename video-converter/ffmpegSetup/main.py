from Programs import ffmpeg
import os
import pathlib

ffmpeg.unzip_ffmpeg()

# add ffmpeg to path
os.environ['PATH'] += os.pathsep + str(pathlib.Path(__file__).parent / "Programs" / "ffmpeg" / "bin")
