import json 
import pprint 
pp = pprint.PrettyPrinter(indent=4)  
import glob 
import os
import pandas as pd

def Intersection(lst1, lst2):
    return list(set(lst1).intersection(lst2))

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
    n = n.replace("c_o_p_y","copy")
    n = n.replace("c_r_e_a_t_e","create")

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
        none_params_list = Intersection(none_params_list, j.keys())
        print(none_params_list)

    folder_name = job_type.replace(":","/").split("/")[:-1]
    folder_name = "../ctm-python-client/new" + "/".join(folder_name).lower() 
    folder_name = folder_name.replace("job","jobs")
    
    #gen file name
    file_name = "../tests/test_" + job_type.replace(":","_") + ".py"
    print(job_type, file_name, job_name)

    #create the file 
    with open(file_name,"w") as f:

        #begin file
        f.write("import unittest,json\n")
        f.write("from ctm-python-client.core import bmc_control_m as ctm-python-client\n")
        f.write("from ctm-python-client." + job_type.replace(":",".").lower().replace("job","jobs") + 
                " import " + job_name + "\n")
        f.write("\n")
        job_name = job_name[0].upper() + job_name[1:]
        
        #Begin class def
        f.write("class Test{}(unittest.TestCase):\n".format(job_name))

        f.write("\tdef test_{}(self):\n".format(job_name))
        f.write("\t\tflow = ctm-python-client.CmJobFlow(application='',sub_application='')\n")
        f.write("\t\tfolder = flow.create_folder('test_folder')\n")
        f.write("\t\tj = {}(folder=folder,job_name='test_job',\n".format(job_name))

        #write Params 
        params = {}
        none_params_list_all = ["Type","RunAs","Host"] + none_params_list
        
        for k in j.keys():
            if k not in none_params_list_all:
                params[k] = gen_name(k) #store params
                f.write("\t\t\t\t{}='{}',\n".format(params[k],params[k]))

        for k in none_params_list:
            params[k] = gen_name(k) #store params
            f.write("\t\t\t\t{}='{}',\n".format(params[k],params[k]))

        # Write default Params for all files
        f.write("\t\t\t\thost=None, run_as=None, description=None)\n")
        
        #Super class init
        f.write("\t\tjobs_params = {}\n".format(set(j.keys())))
        f.write("\t\tjobs_json = j.get_json()\n")
        f.write("\t\ttest_params = set(jobs_json.keys())\n")
        f.write("\t\tprint(test_params)\n")
        f.write("\t\tself.assertEqual(jobs_params,test_params)\n")
        

 






files = glob.glob("jobs/*.json")  
for file in files[:3]: 
    f = open(file) 
    mj = json.load(f) 
    json_to_job(mj)

# for file in files[:1]: 
#     f = open("jobs/Job-Database-EmbeddedQuery.json") 
#     mj = json.load(f) 
#     json_to_job(mj)