from ctm_python_client.jobs.sap.r3.copy import COPYJob

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
fn = os.path.split(__file__)[-1][:-3]
f1 = t1_flow.create_folder(name=fn)
j1 = COPYJob(
      folder=f1,
      job_name='copy',
      connection_profile="SAP-CON",
      sap_job_name="CHILD_1",
      exec="Server",
      target="Server-name",
      job_count="SpecificJob",
      job_count_specific_name="sap-job-1234",
      new_job_name="My-New-Sap-Job",
      start_condition="AfterEvent",
      after_event="HOLA",
      after_event_parameters="parm1 parm2",
      rerun_from_point_of_failure=True,
      copy_from_step="4",
      post_job_action={'Spool': 'CopyToFile', 'SpoolFile': 'spoolfile.log', 'SpoolSaveToPDF': True, 'JobLog': 'CopyToFile', 'JobLogFile': 'Log.txt', 'JobCompletionStatusWillDependOnApplicationStatus': True},
      detect_spawned_job={'DetectAndCreate': 'SpecificJobDefinition', 'JobName': 'Specific-Job-123', 'StartSpawnedJob': True, 'JobEndInControlMOnlyAftreChildJobsCompleteOnSap': True, 'JobCompletionStatusDependsOnChildJobsStatus': True},
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
