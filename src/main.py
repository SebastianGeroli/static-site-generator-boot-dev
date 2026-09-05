import os
import shutil
import sys

from copy_files_recursive import copy_files_recursive
from generate_page import generate_pages_recursive

def main():

    base_path = "/"
    if len(sys.argv) > 0:
        base_path = sys.argv[1]
        print(base_path)
    from_directory = "./static"
    to_directory = "./docs"
    if os.path.exists(to_directory):
        shutil.rmtree(to_directory)
    copy_files_recursive(from_directory,to_directory)
    generate_pages_recursive(base_path,"content","template.html","docs")


if __name__ == "__main__":
    main()