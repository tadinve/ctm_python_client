# Demo: Defining Control_M Workflows using Python

# Step 1 - Setup

## Step 1A - Install the library

# Make sure you have installed the library
# pip install git+https://github.com/controlm/ctm_python_client.git')

import os,sys
print(os.sep)
CURR_PATH = os.path.abspath("")
ctm_path = []
for p in CURR_PATH.split(os.sep):
    ctm_path.append(p)
    if p == "ctm_python_client":
        break
BASE_PATH = os.sep.join(ctm_path)
sys.path.append(BASE_PATH)

from ctm_python_client.core.bmc_control_m import CmJobFlow
from ctm_python_client.jobs.dummy import DummyJob



# Please change the URI, and ctm_user and enter ctm_password 
# to match your environment
# Create a file .secrets with the following three lines. One for uri, one for user and one for password.
"""
https://acb-rhctmv20.centralus.cloudapp.azure.com:8443/automation-api
username
password
"""

with open(os.path.join(BASE_PATH,  ".secrets"), "r") as fp:
    ctm_uri = fp.readline().strip()
    ctm_user = fp.readline().strip()
    ctm_pwd = fp.readline().strip()


## Step 2B - Create the object

from ctm_python_client.session.session import Session

#session = Session(endpoint=ctm_uri, username=ctm_user, password=ctm_pwd)
session = Session(endpoint=ctm_uri, username=ctm_user, password=ctm_pwd)
session.get_token()


t1_flow = CmJobFlow( application="Naga0.2_Demo", sub_application="Demo-02", 
                session=session, ctm_uri=ctm_uri)


## Step 2C - Define the Schedule


t1_flow.set_run_as(username="ctmuser", host="acb-rhctmv20")



# Define the schedule
months = ["JAN", "OCT", "DEC"]
monthDays = ["ALL"]
weekDays = ["MON", "TUE", "WED", "THU", "FRI"]
fromTime = "0300"
toTime = "2100"
t1_flow.set_schedule(months, monthDays, weekDays, fromTime, toTime)


# Step 3  - Create Folder



# Create Fodler
f1 = t1_flow.create_folder(name="HelloWorld")


# Step 4 - Create Tasks



start = t1_flow.add_job(f1, DummyJob(f1, "Start-Flow"))
end = t1_flow.add_job(f1, DummyJob(f1, "End-Flow"))

hello_world_id = t1_flow.add_job(f1, DummyJob(f1, "Hello-World"))


# Step 5 - Chain Tasks



# start >>  hello_world_id >> end
t1_flow.chain_jobs(f1, [start, hello_world_id, end])


# Step 6 - Display Workflow

## Step 6A - Display DAG


# View the t1_flow Details
nodes, edges = t1_flow.get_nodes_and_edges()
nodes, edges


## Step 6B - Display JSON



t1_flow.display_json()


# Step 7 - Submit Workflow to Control-M

t1_flow.deploy()


t1_flow.run()





