# created by ibrahim el-sheikh
# 2022-10-1

import os

# convert video to .wav file by cmd

def convert_video():
    # get file path from user
    file_path = input("Enter file path:- ")
    cmd = f"ffmpeg -i {file_path}  \"E:\cairokey.wav\""
    os.system(cmd)
    print("Done")


convert_video()
