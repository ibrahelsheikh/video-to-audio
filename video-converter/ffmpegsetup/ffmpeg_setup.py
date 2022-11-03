# # dowload file from url then store it in downloads folder then extract it then delete it
#
# import requests
# import os
# import zipfile
#
# url = 'https://www2.census.gov/geo/tiger/GENZ2017/shp/cb_2017_02_tract_500k.zip'
# file_name = 'cb_2017_02_tract_500k.zip'
#
# # download file from url to downloads folder
# def download_file(url):
#     r = requests.get(url, allow_redirects=True)
#     open(file_name, 'wb').write(r.content)
#     pass
# # extract file
# def extract_file(file_name):
#     with zipfile.ZipFile(file_name, 'r') as zip_ref:
#         zip_ref.extractall()
#     my_dir = "D:\\Download\\"
#     my_zip = "D:\\Download\\my_file.zip"
#
#     zip_file = zipfile.ZipFile(my_zip, 'r')
#     for files in zip_file.namelist():
#         zip_file.extract(files, my_dir)
#     zip_file.close()
#
# # delete file
# def delete_file(file_name):
#     os.remove(file_name)
#
#
# if __name__ == '__main__':
#     download_file(url)
#     extract_file(file_name)
#
#     pass


# Python code to convert video to audio
import moviepy.editor as mp

# Insert Local Video File Path
clip = mp.VideoFileClip(r"cairokey.mp4")

# Insert Local Audio File Path
clip.audio.write_audiofile(r"Audio.wav")
