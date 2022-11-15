# created by ibrahim el-sheikh
# 2022-10-1
# tested on python 3.9.7
# successfully tested on windows 11

import os
import pathlib
import shutil


# convert video to .wav file by using ffmpeg
class videoconverter:

    def __init__(self):
        pass

    # create list to store all videos in given directory if given path is directory
    def get_videos_paths(given_path):
        video_paths = []
        if os.path.isdir(given_path):
            for file in os.listdir(given_path):
                if file.endswith(".mp4") or file.endswith(".mkv") \
                        or file.endswith(".avi") or file.endswith(".mov") \
                        or file.endswith(".flv") or file.endswith(".wmv") \
                        or file.endswith(".mpg") or file.endswith(".mpeg") \
                        or file.endswith(".3gp") or file.endswith(".webm") \
                        or file.endswith(".vob") or file.endswith(".m4v") \
                        or file.endswith(".rmvb") or file.endswith(".rm") \
                        or file.endswith(".asf") or file.endswith(".swf") \
                        or file.endswith(".m2ts") or file.endswith(".mts") \
                        or file.endswith(".ts") or file.endswith(".ogv") \
                        or file.endswith(".ogg") or file.endswith(".mxf") \
                        or file.endswith(".dv") or file.endswith(".dvr-ms") \
                        or file.endswith(".amv") or file.endswith(".qt") \
                        or file.endswith(".f4v") or file.endswith(".flv") \
                        or file.endswith(".f4p") or file.endswith(".f4a") \
                        or file.endswith(".f4b"):
                    video_paths.append(given_path + "\\" + file)

        return video_paths

    # convert single video to .wav file
    def video_to_wav(video_path):
        # create output directory

        # get video name without extension
        file_name = pathlib.Path(video_path).stem

        # get video directory
        dir_path = os.path.dirname(video_path)

        # audio path
        audio_path = dir_path + "\\" + file_name + ".wav"

        # check if video exists
        if os.path.exists(video_path):

            # check if audio file exists
            if os.path.exists(audio_path) == False:
                print("video found")
                # convert video to .wav file

                audio_path = os.path.join(dir_path, file_name + ".wav")
                print(audio_path)

                os.system(
                    f"\"ffmpeg -i {video_path}  {dir_path}/{file_name}.wav \"")  # TODO: you can use ffmpeg or moviepy
                print("Done")
            else:
                print("audio file already exists")
        else:
            print("video not found")

    def copytree_audio(src, symlinks=False, ignore=None):
        dst = os.path.join(src, "output")
        if os.path.exists(dst) == False:
            os.mkdir(dst)

        # check if source
        for item in os.listdir(src):
            if os.path.exists(item) == False and item.endswith(
                    ".wav" or ".mp3" or ".m4a" or ".flac" or ".aac" or ".ogg" or ".wma" or ".aiff" or ".alac" or ".amr" or ".ape" or ".au" or ".dct" or ".dss" or ".dvf" or ".flac" or ".gsm" or ".iklax" or ".ivs" or ".m4a" or ".m4b" or ".m4p" or ".mmf" or ".mp3" or ".mpc" or ".msv" or ".nmf" or ".nsf" or ".ogg" or ".oga" or ".mogg" or ".opus" or ".ra" or ".rm" or ".raw" or ".rf64" or ".sln" or ".tta" or ".vox" or ".wav" or ".wma" or ".wv" or ".webm" or ".8svx" or ".cda" or ".mid" or ".midi" or ".rmi" or ".kar" or ".mka" or ".aif" or ".aifc" or ".aiff" or ".m3u" or ".wpl" or ".asx" or ".pls" or ".xspf" or ".m3u" or ".wpl" or ".asx" or ".pls" or ".xspf" or ".mp4" or ".m4v" or ".avi" or ".mov" or ".flv" or ".wmv" or ".mpg" or ".mpeg" or ".3gp" or ".webm" or ".vob" or ".m4v" or ".rmvb" or ".rm" or ".asf" or ".swf" or ".m2ts" or ".mts" or ".ts" or ".ogv" or ".ogg" or ".mxf" or ".dv" or ".dvr-ms" or ".amv" or ".qt" or ".f4v" or ".flv" or ".f4p" or ".f4a" or ".f4b"):
                s = os.path.join(src, item)
                d = os.path.join(dst, item)
                if os.path.isdir(s):
                    shutil.copytree(s, d, symlinks, ignore)
                else:
                    shutil.copy2(s, d)

    # Convert all videos in given directory to .wav files
    def convert(given_path):

        # make output directory

        # copy all audio files to output directory
        videoconverter.copytree_audio(given_path)

        # if pathlib.Path(given_path).is_file() == False:
        #     video_paths = videoconverter.get_videos_paths(given_path)
        #     for video_path in video_paths:
        #         videoconverter.video_to_wav(video_path)
        #
        # else:
        #     videoconverter.video_to_wav(given_path)


videoconverter.convert("D:\music\فرق   خبره.mp4")
