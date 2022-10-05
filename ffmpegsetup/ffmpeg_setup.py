# setup ffmpeg from "https://github.com/GyanD/codexffmpeg/releases/download/2022-10-02-git-5f02a261a2/ffmpeg-2022-10-02-git-5f02a261a2-full_build.zip"
# version 2022-10-02-git-5f02a261a2
# added ffmpeg to path

import requests
import os

global version

version = "ffmpeg-2022-10-02-git-5f02a261a2-full_build.zip"  # TODO :- change version to to your version


# get ffmpeg
def get_ffmpeg(version):
    # check if ffmpeg is already installed
    if os.path.exists(f"C:\\ffmpeg\\bin\\ffmpeg.exe") == False:

        # check if ffmpeg zip exists
        if os.path.exists(f"../ffmpeg.zip") == False:

            # download start
            print("Downloading ffmpeg started   ...")

            ffmpeg_url = str("https://github.com/GyanD/codexffmpeg/releases/download/2022-10-02-git-5f02a261a2/" + version)
            response = requests.get(ffmpeg_url, stream=True)
            with open('ffmpeg.zip', "wb") as f:
                for chunk in response.iter_content(chunk_size=512):
                    if chunk:
                        f.write(chunk)
            print("ffmpeg downloaded successfully")

        else:
            print("ffmpeg already exists")

        os.system("unzip ffmpeg.zip -d ffmpeg")
        # move ffmpeg to c drive
        os.move(f"..\\ffmpeg", "C:\\")
        # add fmmpeg to system path
        os.system("setx /M PATH \"%PATH%;C:\\ffmpeg\\bin\"")

        print("ffmpeg setup successfully")

        # delete ffmpeg zip
        os.remove(f"../{version}")



get_ffmpeg("ffmpeg-2022-10-02-git-5f02a261a2-full_build.zip")


