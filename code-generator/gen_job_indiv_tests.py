import json
import pprint

pp = pprint.PrettyPrinter(indent=4)
import os
from glob import glob
from gen_job_tests_old import gen_name


def read_job_files():

    # root_dir needs a trailing slash (i.e. /root/dir/)
    root_dir = "ctm_python_client/jobs/**/*.py"
    files = [
        f
        for f in glob(root_dir, recursive=True)
        if os.path.isfile(f) and f[-5:] != "__.py"
    ]
    return files


def get_class_from_file(fn):

    # since the dir name is same as lib path name, replace / with .
    lib = fn[:-3].replace("/", ".")

    # init variables so, return does not fail on empty file
    start_collecting = False
    class_nm = ""
    params = []

    f = open(fn, "r")
    for line in f:
        # remove trailing and leading spaces
        line = line.strip()

        # ignore empty lines
        if len(line) == 0:
            continue

        # this where we see the class object defn
        if line[:5] == "class":
            class_nm = line.split(" ")[1].split("(")[0]

        # start capturing params for class
        if line.strip() == "def __init__(":
            start_collecting = True

        # collect params

        if start_collecting and line[-1] == ",":
            param = line[:-1]
            # ignore default params for now
            if "=" in param or param == "self":
                continue
            rvalue = f"'{param}'"
            if param == "folder":
                rvalue = "f1"
            if param == "job_name":
                rvalue = f"'{class_nm.lower()}_job'"
            params.append(f"{param} = {rvalue},")

        # reached end of class def, so break
        if line == "):":
            break

    return lib, class_nm, params


def write_flow_code(f, flow_code):
    BASE_PATH = os.path.abspath(os.path.dirname(__file__))
    fp = open(BASE_PATH + flow_code, "r")
    for line in fp:
        f.write(line)


def get_json_fp(job_name):
    BASE_PATH = os.path.abspath(os.path.dirname(__file__))
    files = os.listdir(BASE_PATH + "/jobs/")
    fp = None
    print(job_name)
    for file in files:
        if job_name.lower() in file.lower():
            fp = open(BASE_PATH + "/jobs/" + file, "r")
    return fp


def gen_job_class(j, f):
    job_name = j[:-3]

    fp = get_json_fp(job_name)
    jobs_json = json.load(fp)
    f.write(f"j1 = {j}(\n")
    f.write(f"      folder=f1,\n")
    f.write(f"      job_name='{job_name.lower()}',\n")

    for k, v in jobs_json.items():
        if k == "Type" or gen_name(k) == "job_name":
            continue
        rvalue = v
        if isinstance(rvalue, str):
            rvalue = f'"{v}"'
        f.write(f"      {gen_name(k)}={rvalue},\n")
    f.write("      )\n")
    f.write("t1_flow.add_job(folder=f1, job=j1)\n\n")

    return job_name


if __name__ == "__main__":

    # get all python job files
    files = read_job_files()
    imports = []

    # generate info for each python job class
    for f in files[:50]:
        print(f)
        imports.append(get_class_from_file(f))
    for i in imports:
        if i[1] in [
            "InformaticaJob",
            "AiGenericJob",
            "ADFJob",
            "AIBlobStorageJob",
            "StoredProcedureJob",
            "AIMonitorRemoteJob",
            "FWCreateJob",
            "ProcessChainJob",
        ]:
            continue
        with open(f"tests/tests_indiv_jobs/test_{i[1].lower()}.py", "w") as f:
            # dump all the job imports at the top
            f.write(f"from {i[0]} import {i[1]}\n")
            f.write(f"\n")

            # generate jobflow, create folder and session code here
            write_flow_code(f, "/all_jobs_begin.py")

            # # Generete the test function for each job

            gen_job_class(i[1], f)

            write_flow_code(f, "/all_jobs_end.py")
