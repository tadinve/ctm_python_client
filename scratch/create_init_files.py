import glob

for filename in glob.iglob(root_dir + '**/**', recursive=True):
     print(filename)


import os

for dirname, dirnames, filenames in os.walk('../newjobs/.'):
    # print path to all subdirectories first.
    for subdirname in dirnames:
        print(os.path.join(dirname, subdirname))