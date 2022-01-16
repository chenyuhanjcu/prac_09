"""
CP1404/CP5632 Practical
Sort Files Program 2
"""

import os
import shutil


def main():
    """Sort Files with file extension."""
    os.chdir('FilesToSort')
    file_extensions = []
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        file_extension = filename.split(".")[-1]
        if file_extension not in file_extensions:
            file_extensions.append(file_extension)
    for file_extension in file_extensions:
        directory_name = input(f"What category would you like to sort {file_extension} files into? ")
        try:
            os.mkdir(directory_name)
        except FileExistsError:
            pass
        for filename in os.listdir('.'):
            if os.path.isfile(filename) and filename.endswith(file_extension):
                shutil.move(filename, directory_name)


main()
