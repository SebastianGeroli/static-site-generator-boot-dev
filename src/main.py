import os
import shutil

from copy_files_recursive import copy_files_recursive
from generate_page import generate_page

def main():
    from_directory = "./static"
    to_directory = "./public"
    if os.path.exists(to_directory):
        shutil.rmtree(to_directory)
    copy_files_recursive(from_directory,to_directory)
    generate_page("content/index.md","template.html","public/index.html")

if __name__ == "__main__":
    main()