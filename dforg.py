import os, shutil
import extensions as ext

for folder in ext.FORMAT_DICTIONARY.keys():

    try:
        os.mkdir(folder)
    except FileExistsError:
        continue

ls = [f for f in os.listdir('.') if os.path.isfile(f)]

print('program is done executing')