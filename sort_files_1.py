"""
CP1404/CP5632 Practical
Sort Files Program
"""

import os
import shutil


def main():
    """Sort Files with file extension"""
    os.chdir('FilesToSort')
    print(os.getcwd())
    print(os.listdir('.'))
    # os.mkdir('')
    for filename in os.listdir('.'):
        file_name = filename.split(".")
        directory_name = file_name[-1]
        try:
            os.mkdir(directory_name)
        except FileExistsError:
            pass
        if os.path.isfile(filename):
            shutil.move(filename, directory_name)


main()
