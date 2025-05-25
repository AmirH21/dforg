import os, shutil

FOLDERNAMES = ['Compressed', 'Documents', 'Videos', 'Other']

for name in FOLDERNAMES:
    
    try:
        os.mkdir(name)
    except FileExistsError:
        continue



print('program is done executing')