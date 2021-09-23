from ctm_python_client.jobs.hadoop.pig import PigJob

import os
from ctm_python_client.core.bmc_control_m import CmJobFlow
from ctm_python_client.session.session import Session

BASE_PATH = os.path.abspath(os.path.dirname(__file__))
with open(BASE_PATH + "/.secrets", "r") as fp:
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
fn = __file__.split("/")[-1][:-3]
f1 = t1_flow.create_folder(name=fn)
j1 = PigJob(
      folder=f1,
      job_name='pig',
      connection_profile="DEV_CLUSTER",
      pig_script="/home/user/script.pig",
      host="edgenode",
      parameters=[{'amount': '1000'}, {'volume': '120'}],
      pre_commands={'FailJobOnCommandFailure': False, 'Commands': [{'get': 'hdfs://nn.example.com/user/hadoop/file localfile'}, {'rm': 'hdfs://nn.example.com/file /user/hadoop/emptydir'}]},
      post_commands={'FailJobOnCommandFailure': True, 'Commands': [{'put': 'localfile hdfs://nn.example.com/user/hadoop/file'}]},
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


def test_output():
    assert j["successful_smart_folders_count"] == 1
