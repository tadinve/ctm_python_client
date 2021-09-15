import json
import pprint

pp = pprint.PrettyPrinter(indent=4)
import os
from glob import glob

def read_job_files():

    # root_dir needs a trailing slash (i.e. /root/dir/)
    root_dir = "ctm_python_client/jobs/**/*.py"
    files = [f for f in glob(root_dir, recursive=True) if os.path.isfile(f) and f[-5:] != "__.py"]
    return files

def get_class_from_file(fn):
    
    f = open(fn, "r")
    lib = fn[:-3].replace('/','.')
    for line in f:
        if line[:5] == "class":
            class_nm = line.split(" ")[1].split("(")[0]
            return  lib,class_nm

if __name__ == '__main__':
    files = read_job_files()
    imports = []
    for f in files:
        imports.append(get_class_from_file(f))
    
    with open("tests/test_all_jobs.py","w") as f:
        for i in imports:
            f.write(f"from {i[0]} import {i[1]}\n")
        
        f.write(f"\n")

        for i in imports:
            f.write(f"def test_{i[1]}():\n")
            f.write(f"    assert 1==1 \n")
            f.write(f"\n")

