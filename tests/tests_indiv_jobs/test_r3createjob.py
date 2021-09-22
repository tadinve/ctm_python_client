from ctm_python_client.jobs.sap.r3.create import R3CREATEJob

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
fn = __file__.split('/')[-1][:-3]
f1 = t1_flow.create_folder(name=fn)
j1 = R3CREATEJob(
      folder=f1,
      job_name='r3create',
      connection_profile="SAPCP",
      sap_job_name="SAP_job2",
      start_condition="Immediate",
      rerun_from_step="3",
      target="controlmserver",
      created_by="user1",
      steps=[{'StepType': 'ABAP', 'TimeToPrint': 'PrintLater', 'CoverPrintPage': True, 'OutputDevice': 'prt', 'UserName': 'user', 'SpoolAuthorization': 'Auth', 'CoverDepartment': 'dpt', 'SpoolListName': 'spoolname', 'OutputNumberRows': '62', 'NumberOfCopies': '5', 'NewSpoolRequest': False, 'PrintArchiveMode': 'PrintAndArchive', 'CoverPage': 'Print', 'ArchiveObjectType': 'objtype', 'SpoolListTitles': 'titles', 'OutputLayout': 'layout', 'CoverSheet': 'Print', 'ProgramName': 'ABAP_PROGRAM', 'Language': 'e', 'ArchiveInformationField': 'inf', 'DeleteAfterPrint': True, 'PrintExpiration': '3', 'OutputNumberColumns': '88', 'ArchiveDocumentType': 'doctype', 'CoverRecipient': 'recipient', 'VariantName': 'NameOfVariant', 'VariantParameters': [{'Type': 'Range', 'High': '2', 'Sign': 'I', 'Option': 'BT', 'Low': '1', 'Name': 'var1', 'Modify': False}, {'Low': '5', 'Type': 'Range', 'Option': 'BT', 'Sign': 'I', 'Modify': True, 'High': '6', 'Name': 'var3'}]}, {'StepType': 'ABAP', 'PrintArchiveMode': 'Print', 'ProgramName': 'ABAP_PROGRAM2', 'VariantName': 'Myvar_with_temp', 'TemporaryVariantParameters': [{'Type': 'Simple', 'Name': 'var', 'Value': 'P11'}, {'Type': 'Simple', 'Name': 'var2', 'Value': 'P11'}]}],
      post_job_action={'JobLog': 'CopyToFile', 'JobCompletionStatusWillDependOnApplicationStatus': True, 'SpoolSaveToPDF': True, 'JobLogFile': 'fileToCopy.txt'},
      spool_list_recipient={'ReciptNoForwarding': False},
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
