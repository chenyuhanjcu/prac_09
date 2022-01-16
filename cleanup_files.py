"""
CP1404/CP5632 Practical
Demos of various os module examples
"""

import os


def main():
    """Cleanup inconsistent song lyrics file names."""

    # Change to desired directory
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        # print("Directory:", directory_name)
        # print("\tcontains subdirectories:", subdirectories)
        # print("\tand files:", filenames)
        # print("(Current working directory is: {})".format(os.getcwd()))

        for filename in filenames:
            new_name = get_fixed_filename(filename)
            print("Renaming {} to {}".format(filename, new_name))

            full_name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, new_name)
            os.rename(full_name, new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    file_name = filename.split(".")  # split .txt with prefix
    prefix = file_name[0]   # only keep prefix now
    new_prefix = ""
    for index, char in enumerate(prefix):
        if char.isupper() and index != 0 and prefix[index - 1] != " ":
            char = " " + char
        new_prefix += char  # separate different words
    capital_prefix = ""
    for chuck in new_prefix.split():
        chuck = chuck.title()
        capital_prefix += chuck + "_"  # create capitalized words with "_"
    capital_prefix = capital_prefix[:-1]
    new_name = capital_prefix + ".txt"  # add txt file type
    return new_name


def clean_name_test():
    print(get_fixed_filename("Away In A Manger.txt"))
    print(get_fixed_filename("ItIsWell (oh my soul).txt"))
    print(get_fixed_filename("O little town of bethlehem.TXT"))
    print(get_fixed_filename("SilentNight.TXT"))


clean_name_test()
# main()
