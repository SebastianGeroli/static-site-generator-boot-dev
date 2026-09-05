import os
import shutil

from copy_files_recursive import copy_files_recursive
from generate_page import generate_pages_recursive

def main():
    from_directory = "./static"
    to_directory = "./public"
    if os.path.exists(to_directory):
        shutil.rmtree(to_directory)
    copy_files_recursive(from_directory,to_directory)
    generate_pages_recursive("content","template.html","public")


if __name__ == "__main__":
    main()