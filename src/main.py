import os
import shutil

from textnode import TextNode, TextType

def main():
    from_directory = "../static"
    to_directory = "../public" 
    make_copy(from_directory,to_directory)


def make_copy(from_directory:str, to_directory:str):
    if os.path.exists(from_directory):
        if not os.path.exists(to_directory):
            os.mkdir(to_directory)
        for entry in os.listdir(from_directory):
            from_path = os.path.join(from_directory, entry)
            to_path = os.path.join(to_directory, entry)
            if os.path.isfile(from_path):
                if os.path.exists(to_path):
                    shutil.rmtree(to_path)
                shutil.copy(from_path, to_path)
            if os.path.isdir(from_path):
               make_copy(from_path, to_path)
if __name__ == "__main__":
    main()