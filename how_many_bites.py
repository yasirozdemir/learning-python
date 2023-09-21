import os
from os import path


def how_many_bites(file_ext):
    cwd = os.getcwd()  # cwd -> current working directory
    files = os.listdir(cwd)
    text_files_size = 0
    for file in files:
        if file.endswith("." + file_ext):
            file_path = path.join(cwd, file)
            try:
                file_size = path.getsize(file_path)
                text_files_size += file_size
            except FileExistsError as e:
                print(e)  # throw an error if the file not found
    return text_files_size
