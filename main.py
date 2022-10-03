# create by Ibrahim elsheikh
# at 2022-10-1

import os
import pathlib

given_path = "E:\cairokey.mp4"



output_dirictory_path = os.path.dirname(given_path) + "\\output"
def is_file_or_dirictory(path):
    if os.path.isdir(path):
        return "dirictory"
    elif os.path.isfile(path):
        return "file"
    else:
        return "not found"


# check if output dirictory exists if not create it if yes pass
if os.path.exists(output_dirictory_path) == False:
    os.mkdir(output_dirictory_path)
    print("output dirictory created")
else:
    print("output dirictory already exists")
