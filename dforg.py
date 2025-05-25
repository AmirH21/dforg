import os, shutil

FOLDERNAMES = ['Compressed', 'Documents', 'Videos','Music', 'Other']

for name in FOLDERNAMES:
    
    try:
        os.mkdir(name)
    except FileExistsError:
        continue

# ls = [f for f in os.listdir('.') if os.path.isfile(f)]

print('program is done executing')