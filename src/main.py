import os
import shutil
import sys

from copy_static_to_public import copy_files_recursive
from generate_page import generate_page, generate_page_recursively

dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"


def main():
    if len(sys.argv) < 2:
        basepath = "/"
    else:
        basepath = sys.argv[1]
    

    print("Deleting docs directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to docs directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating page...")
    generate_page_recursively(
        dir_path_content,
        template_path,
        dir_path_public,
        basepath
    )


main()






