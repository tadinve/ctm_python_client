from ctm_python_client.jobs.informatica import InformaticaJob

import os
from ctm_python_client.core.bmc_control_m import CmJobFlow
from ctm_python_client.session.session import Session

BASE_PATH = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(BASE_PATH,  ".secrets"), "r") as fp:
    ctm_uri = fp.readline().strip()
    ctm_user = fp.readline().strip()
    ctm_pwd = fp.readline().strip()

# Create CTM Session
session = Session(endpoint=ctm_uri, username=ctm_user, password=ctm_pwd)

# CREATE JOB FLOW
t1_flow = CmJobFlow(
    application="Naga0.3_Test", sub_application="TestAllJobs", session=session
)

t1_flow.set_run_as(username="ctmuser", host="acb-rhctmv20")

# Define the schedule
months = ["JAN", "OCT", "DEC"]
monthDays = ["ALL"]
weekDays = ["MON", "TUE", "WED", "THU", "FRI"]
fromTime = "0300"
toTime = "2100"
t1_flow.set_schedule(months, monthDays, weekDays, fromTime, toTime)

# Create Folder
f1 = t1_flow.create_folder(name="TestAllJobs")
j1 = InformaticaJob(
    folder=f1,
    job_name="informatica",
    connection_profile="INFORMATICA_CONNECTION",
    repository_folder="POC",
    workflow="WF_Test",
    instance_name="MyInstamce",
    os_profile="MyOSProfile",
    workflow_execution_mode="RunSingleTask",
    run_single_task="s_MapTest_Success",
    workflow_restart_mode="ForceRestartFromSpecificTask",
    restart_from_task="s_MapTest_Success",
    workflow_parameters_file="/opt/wf1.prop",
)
t1_flow.add_job(folder=f1, job=j1)

import json

x = t1_flow.deploy()
s = str(x[0])
s = s.replace("'", '"')
s = s.replace("None", '"None"')
s = s.replace("False", '"False"')
s = s.replace("True", '"True"')
s = s.replace("\n", "")
j = json.loads(s)
assert j["successful_smart_folders_count"] == 1
