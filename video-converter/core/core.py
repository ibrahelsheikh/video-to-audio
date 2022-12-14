# created by ibrahim el-sheikh
# 2022-10-1
# tested on python 3.9.7
# successfully tested on windows 11

import os
import pathlib
import shutil


# convert video to .wav file by using ffmpeg
class main:

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
        output_path = dir_path + "\\" + file_name + ".wav"

        # check if video exists
        if os.path.exists(video_path):

            # check if audio file exists
            if os.path.exists(output_path) == False:
                print("video found")
                # convert video to .wav file

                output_path = os.path.join(dir_path, file_name + ".wav")
                print(output_path)

                os.system(
                    f"ffmpeg -i {video_path}  {output_path}{file_name}.wav")  # TODO: you can use ffmpeg or moviepy
                print("Done")
            else:
                print("audio file already exists")
        else:
            print("video not found")


    # Convert all videos in given directory to .wav files
    def convert(given_path):

        # rename dir
        new_given_path = given_path.replace(" ", "_")
        if given_path != new_given_path:
        os.rename(given_path, new_given_path)
        print (new_given_path)

        if pathlib.Path(new_given_path).is_file() == False:
            video_paths = main.get_videos_paths(new_given_path)
            for video_path in video_paths:
                main.video_to_wav(video_path)

        else:
            main.video_to_wav(new_given_path)


main.convert("D:\\music")  # TODO: change this to your path
