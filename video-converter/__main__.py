from VideoConverter.core import core
from ffmpegSetup import main

if __name__ == '__main__':
    core.videoconverter.video_to_wav("D:\\Newfolder\\love-adham.mp4")
    # qdd ffmpeg to path
    main.get_ffmpeg_path()
    # add ffmpeg to path
