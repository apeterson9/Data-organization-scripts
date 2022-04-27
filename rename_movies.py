# This script will rename files that end in .avi so they are compatible with the motility package.
# Renames according to the last word following a space

import os, shutil, pandas as pd, xlsxwriter
from pathlib import Path


# Path('my_file.mp3').suffix == '.mp3'

user_input = input('Enter a directory containing movies that need to be renamed\n')
print(f'Accessing {user_input}')
assert os.path.exists(user_input), "I did not find the directory at, "+str(user_input)
print("Hooray we found your directory!")
print(os.listdir(user_input))

for file in os.listdir(user_input):
    print(file)
    if Path(file).suffix == '.avi':
        old_name = file
        first, *last = old_name.split()
        os.rename(old_name, last)

