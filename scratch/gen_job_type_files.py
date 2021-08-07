import json 
import pprint 
pp = pprint.PrettyPrinter(indent=4)  
import glob 
import os
import pandas as pd


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
    n = n.replace("a_i_","ai")
    n = n.replace("s_s_i_s","ssis")
    n = n.replace("h_d_f_s","hdfs")

    return n

def get_job_name(s):
    s =  s.split(":")[-1]
    return "".join(s)

def json_to_job(j):

    df = pd.read_csv("jobs/none_params.csv",sep=",",index_col=0)
    jt = list(df.index.values)
    print("jt=",jt)
    job_type = j["Type"]
    if job_type[-3:] != "Job":
        job_name = get_job_name(job_type) + "Job"
    else:
        job_name = get_job_name(job_type)
    job_name = job_name.replace(" ","")
    print("JobName =",job_name)

    none_params_list = []
    if job_name in jt:
        none_params_list = df.loc[job_name].values.tolist()
        print(none_params_list)

    folder_name = job_type.replace(":","/").split("/")[:-1]
    folder_name = "../naga/new" + "/".join(folder_name).lower() 
    folder_name = folder_name.replace("job","jobs")
    file_name = folder_name + "/" + gen_name(job_name)[:-4] + ".py"
    file_name = file_name.replace("Job","").lower()
    print(job_type, file_name, job_name)

    #Create directory if it does not exist
    try:
        os.makedirs(folder_name)
        with open(folder_name+"/__init__.py","w") as f:
            f.write("")
    except FileExistsError:
        # directory already exists
        pass

    #create the file 
    with open(file_name,"w") as f:

        #begin file
        f.write("from naga.jobs.base import BaseJob\n")
        f.write("\n")
        job_name = job_name[0].upper() + job_name[1:]
        
        #Begin class def
        f.write("class {}(BaseJob):\n".format(job_name))
        f.write("\tdef __init__(self, folder, job_name, \n")

        #write Params 
        params = {}
        none_params_list_all = ["Type","RunAs","Host"] + none_params_list
        for k in j.keys():
            if k not in none_params_list_all:
                params[k] = gen_name(k) #store params
                f.write("\t\t\t\t{},\n".format(params[k]))

        for k in none_params_list:
            params[k] = gen_name(k) #store params
            f.write("\t\t\t\t{} = None,\n".format(params[k]))

        # Write default Params for all files
        f.write("\t\t\t\thost=None, run_as=None, description=None):\n")
        
        #Super class init
        f.write("\n\t\tBaseJob.__init__(self, folder, job_name, description=description, host=host, run_as=run_as)\n")
        
        #Init and store all params
        for k in params:
            f.write("\t\tself.{} = {}\n".format(params[k],params[k]))              
        f.write("\n")

        #begin get_json method
        f.write("\tdef get_json(self):\n")
        f.write("\t\tjob_json = BaseJob.get_json(self)\n")
        f.write("\t\tjob_json['Type'] = '{}'\n".format(job_type))
        for k in params:
            f.write("\t\tif self.{} != None:\n".format(params[k]))             
            f.write("\t\t\tjob_json['{}'] = self.{}\n".format(k,params[k]) )
        f.write("\t\treturn job_json\n")

 






files = glob.glob("jobs/*.json")  
# for file in files[:]: 
#     f = open(file) 
#     mj = json.load(f) 
#     json_to_job(mj)

for file in files[:1]: 
    f = open("jobs/Job-Database-EmbeddedQuery.json") 
    mj = json.load(f) 
    json_to_job(mj)

fn = "/__init__.py"
root_dir = '../naga/newjobs'
open(root_dir+fn, 'a').close()

for dirname, dirnames, filenames in os.walk(root_dir):
    # print path to all subdirectories first.

    for subdirname in dirnames:
        dn = os.path.join(dirname, subdirname)
        open(dn+fn, 'a').close()