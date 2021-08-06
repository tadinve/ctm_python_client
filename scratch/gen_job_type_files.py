import json 
import pprint 
pp = pprint.PrettyPrinter(indent=4)  
import glob 
import os

def gen_name(n):
    import re
    n = n.replace(" ","")
    n = n.replace("-","_")
    n = n.replace("__","_")
    n = re.sub('([A-Z]{1})', r'_\1',n).lower()
    if n[0] == "_":
        n = n[1:]
    n = n.replace("__","_")
    n = n.replace("s_q_l","sql")
    n = n.replace("a_w_s","aws")
    n = n.replace("s_a_p","sap")
    n = n.replace("g_l_u_e","glue")
    n = n.replace("a_d_f","adf")
    n = n.replace("s_l_a","sla")
    n = n.replace("a_i_","ai_")

    return n

def get_job_name(s):
    s =  s.split(":")[-1]
    return gen_name(s)
def json_to_job(j):
    job_type = j["Type"]
    if job_type[-3:] != "Job":
        job_name = get_job_name(job_type) + "Job"
    else:
        job_name = get_job_name(job_type)
    job_name = job_name.replace(" ","_")
    folder_name = job_type.replace(":","/").split("/")[:-1]
    folder_name = "../naga/new" + "/".join(folder_name).lower() 
    folder_name = folder_name.replace("job","jobs")
    file_name = folder_name + "/" + job_name + ".py"
    file_name = file_name.replace("Job","").lower()
    print(job_type, file_name, job_name)
    try:
        os.makedirs(folder_name)
        with open(folder_name+"/__init__.py","w") as f:
            f.write("")

    except FileExistsError:
        # directory already exists
        pass
    with open(file_name,"w") as f:
        params = {}
        f.write("from naga.jobs.base import BaseJob\n")
        f.write("\n")
        f.write("class {}(BaseJob):\n".format(job_name))
        f.write("\tdef __init__(self, folder, job_name, \n")
        for k in j.keys():
            if k not in ["Type","RunAs","Host"]:
                params[k] = gen_name(k)
                f.write("\t\t\t\t{},\n".format(params[k]))
        f.write("\t\t\thost=None, run_as=None, description=None):\n")
        f.write("\t\tBaseJob.__init__(self, folder, job_name, description=description, host=host, run_as=run_as)\n")
        for k in params:
            f.write("\t\tself.{} = {}\n".format(params[k],params[k]))      
        
        f.write("\n")
        f.write("\tdef get_json(self):\n")
        f.write("\t\tjob_json = BaseJob.get_json(self)\n")
        f.write("\t\tjob_json['Type'] = '{}'\n".format(job_type))
        for k in params:
            f.write("\t\tif self.{} != None:\n".format(params[k]))             
            f.write("\t\t\tjob_json['{}'] = self.{}\n".format(k,params[k]) )
        f.write("\t\treturn job_json\n")

 






files = glob.glob("jobs/*.json")  
for file in files[:]: 
    f = open(file) 
    mj = json.load(f) 
    json_to_job(mj)