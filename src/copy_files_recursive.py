import os
import shutil


def copy_files_recursive(from_directory:str, to_directory:str):
    if not os.path.exists(to_directory):
        os.mkdir(to_directory)

    for file_name in os.listdir(from_directory):
        from_path = os.path.join(from_directory, file_name)
        to_path = os.path.join(to_directory, file_name)
        if os.path.isfile(from_path):
            shutil.copy(from_path, to_path)
        else:
            copy_files_recursive(from_path, to_path)