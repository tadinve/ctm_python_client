from ctm_python_client.jobs.command import CommandJob
from ctm_python_client.jobs.people_soft import PeopleSoftJob
from ctm_python_client.jobs.file_transfer import FileTransferJob
from ctm_python_client.jobs.sla_management import SLAManagementJob
from ctm_python_client.jobs.informatica import InformaticaJob
from ctm_python_client.jobs.embedded_script import EmbeddedScriptJob
from ctm_python_client.jobs.script import ScriptJob
from ctm_python_client.jobs.dummy import DummyJob
from ctm_python_client.jobs.adf import ADFJob
from ctm_python_client.jobs.ai_jobs.ai_generic import AiGenericJob
from ctm_python_client.jobs.ai_jobs.ai_blob_storage import AIBlobStorageJob
from ctm_python_client.jobs.database.stored_procedure import StoredProcedureJob
from ctm_python_client.jobs.database.sql_script import SQLScriptJob
from ctm_python_client.jobs.database.embedded_query import EmbeddedQueryJob
from ctm_python_client.jobs.database.mssql.agent import AgentJob
from ctm_python_client.jobs.database.mssql.ssis import SSISJob
from ctm_python_client.jobs.filewatcher.delete import DeleteJob
from ctm_python_client.jobs.filewatcher.create import FWCreateJob
from ctm_python_client.jobs.sap.bw.process_chain import ProcessChainJob
from ctm_python_client.jobs.sap.r3.create import R3CREATEJob
from ctm_python_client.jobs.sap.r3.copy import COPYJob
from ctm_python_client.jobs.azure.batch_account import BatchAccountJob
from ctm_python_client.jobs.azure.logic_apps import LogicAppsJob
from ctm_python_client.jobs.azure.function import FunctionJob
from ctm_python_client.jobs.hadoop.sqoop import SqoopJob
from ctm_python_client.jobs.hadoop.hdfs_commands import HDFSCommandsJob
from ctm_python_client.jobs.hadoop.hdfs_file_watcher import HDFSFileWatcherJob
from ctm_python_client.jobs.hadoop.mapred_streaming import MapredStreamingJob
from ctm_python_client.jobs.hadoop.dist_cp import DistCpJob
from ctm_python_client.jobs.hadoop.hive import HiveJob
from ctm_python_client.jobs.hadoop.oozie import OozieJob
from ctm_python_client.jobs.hadoop.map_reduce import MapReduceJob
from ctm_python_client.jobs.hadoop.pig import PigJob
from ctm_python_client.jobs.hadoop.tajo.query import TajoQueryJob
from ctm_python_client.jobs.hadoop.tajo.input_file import InputFileJob
from ctm_python_client.jobs.hadoop.spark.python import PythonJob
from ctm_python_client.jobs.hadoop.spark.scala_java import ScalaJavaJob
from ctm_python_client.jobs.aws.aws_lambda import LambdaJob
from ctm_python_client.jobs.aws.batch import BatchJob
from ctm_python_client.jobs.aws.step_function import StepFunctionJob

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


j1 = CommandJob(
    folder=f1,
    job_name="command",
    command="echo hello",
    pre_command="echo before running main command",
    post_command="echo after running main command",
    host="myhost.mycomp.com",
    run_as="user1",
)
t1_flow.add_job(folder=f1, job=j1)

j1 = PeopleSoftJob(
    folder=f1,
    job_name="peoplesoft",
    connection_profile="PS_CONNECT",
    user="PS_User3",
    control_id="ControlId",
    server_name="ServerName",
    process_type="ProcessType",
    process_name="ProcessName",
    append_to_output=False,
    bind_variables=["value1", "value2"],
    run_as="controlm",
)
t1_flow.add_job(folder=f1, job=j1)

j1 = FileTransferJob(
    folder=f1,
    job_name="filetransfer",
    connection_profile_src="amazonConn",
    connection_profile_dest="LocalConn",
    number_of_retries="4",
    s3_bucket_name="bucket1",
    host="agentHost",
    file_transfers=[
        {"Src": "folder/sub_folder/file1", "Dest": "folder/sub_folder/file2"}
    ],
)
t1_flow.add_job(folder=f1, job=j1)

j1 = SLAManagementJob(
    folder=f1,
    job_name="slamanagement",
    service_name="SLA-GOOD",
    service_priority="1",
    created_by="emuser",
    run_as="DUMMYUSR",
    job_runs_deviations_tolerance="2",
    complete_in={"Time": "00:01"},
    events_to_wait_for={
        "Type": "WaitForEvents",
        "Events": [{"Event": "Hello-TO-SLA_Job_for_SLA-GOOD"}],
    },
    events_to_delete={
        "Type": "DeleteEvents",
        "Events": [{"Event": "Hello-TO-SLA_Job_for_SLA-GOOD"}],
    },
)
t1_flow.add_job(folder=f1, job=j1)

j1 = EmbeddedScriptJob(
    folder=f1,
    job_name="embeddedscript",
    script="echo 'Hello world'",
    host="myhost.mycomp.com",
    run_as="user1",
    file_name="myscript.sh",
    pre_command="echo before running script",
    post_command="echo after running script",
)
t1_flow.add_job(folder=f1, job=j1)

j1 = ScriptJob(
    folder=f1,
    job_name="script",
    file_name="task1123.sh",
    file_path="/home/user1/scripts",
    pre_command="echo before running script",
    post_command="echo after running script",
    host="myhost.mycomp.com",
    run_as="user1",
)
t1_flow.add_job(folder=f1, job=j1)

j1 = DummyJob(
    folder=f1,
    job_name="dummy",
)
t1_flow.add_job(folder=f1, job=j1)

j1 = SQLScriptJob(
    folder=f1,
    job_name="sqlscript",
    host="AgentHost",
    sql_script="/home/controlm/sqlscripts/selectOrclParm.sql",
    connection_profile="ORACLE_CONNECTION_PROFILE",
    parameters=[
        {"firstParamName": "firstParamValue"},
        {"secondParamName": "secondParamValue"},
    ],
)
t1_flow.add_job(folder=f1, job=j1)

j1 = EmbeddedQueryJob(
    folder=f1,
    job_name="embeddedquery",
    connection_profile="POSTGRESQL_CONNECTION_PROFILE",
    query="SELECT %%firstParamName AS VAR1 n FROM DUMMY n ORDER BY  VAR1 DESC",
    host="${agentName}",
    run_as="PostgressCP",
    variables=[{"firstParamName": "firstParamValue"}],
    autocommit="N",
    output_execution_log="Y",
    output_sql_output="Y",
    sql_output_format="XML",
)
t1_flow.add_job(folder=f1, job=j1)

j1 = AgentJob(
    folder=f1,
    job_name="agent",
    connection_profile="MSSQL-WE-EXAMPLE",
    host="agentHost",
    category="Data Collector",
)
t1_flow.add_job(folder=f1, job=j1)

j1 = SSISJob(
    folder=f1,
    job_name="ssis",
    connection_profile="MSSQL-CP-NAME",
    host="agentHost",
    package_source="SSIS Package Store",
    package_name="\Data Collector\SqlTraceCollect",
    config_files=[
        "C:\\Users\\dbauser\\Desktop\\test.dtsConfig",
        "C:\\Users\\dbauser\\Desktop\\test2.dtsConfig",
    ],
    properties=[{"PropertyName": "PropertyValue"}, {"PropertyName2": "PropertyValue2"}],
)
t1_flow.add_job(folder=f1, job=j1)

j1 = DeleteJob(
    folder=f1,
    job_name="delete",
    run_as="controlm",
    path="C:/path.txt",
    search_interval="45",
    time_limit="22",
    start_time="201805041535",
    stop_time="201905041535",
)
t1_flow.add_job(folder=f1, job=j1)

j1 = R3CREATEJob(
    folder=f1,
    job_name="r3create",
    connection_profile="SAPCP",
    sap_job_name="SAP_job2",
    start_condition="Immediate",
    rerun_from_step="3",
    target="controlmserver",
    created_by="user1",
    steps=[
        {
            "StepType": "ABAP",
            "TimeToPrint": "PrintLater",
            "CoverPrintPage": True,
            "OutputDevice": "prt",
            "UserName": "user",
            "SpoolAuthorization": "Auth",
            "CoverDepartment": "dpt",
            "SpoolListName": "spoolname",
            "OutputNumberRows": "62",
            "NumberOfCopies": "5",
            "NewSpoolRequest": False,
            "PrintArchiveMode": "PrintAndArchive",
            "CoverPage": "Print",
            "ArchiveObjectType": "objtype",
            "SpoolListTitles": "titles",
            "OutputLayout": "layout",
            "CoverSheet": "Print",
            "ProgramName": "ABAP_PROGRAM",
            "Language": "e",
            "ArchiveInformationField": "inf",
            "DeleteAfterPrint": True,
            "PrintExpiration": "3",
            "OutputNumberColumns": "88",
            "ArchiveDocumentType": "doctype",
            "CoverRecipient": "recipient",
            "VariantName": "NameOfVariant",
            "VariantParameters": [
                {
                    "Type": "Range",
                    "High": "2",
                    "Sign": "I",
                    "Option": "BT",
                    "Low": "1",
                    "Name": "var1",
                    "Modify": False,
                },
                {
                    "Low": "5",
                    "Type": "Range",
                    "Option": "BT",
                    "Sign": "I",
                    "Modify": True,
                    "High": "6",
                    "Name": "var3",
                },
            ],
        },
        {
            "StepType": "ABAP",
            "PrintArchiveMode": "Print",
            "ProgramName": "ABAP_PROGRAM2",
            "VariantName": "Myvar_with_temp",
            "TemporaryVariantParameters": [
                {"Type": "Simple", "Name": "var", "Value": "P11"},
                {"Type": "Simple", "Name": "var2", "Value": "P11"},
            ],
        },
    ],
    post_job_action={
        "JobLog": "CopyToFile",
        "JobCompletionStatusWillDependOnApplicationStatus": True,
        "SpoolSaveToPDF": True,
        "JobLogFile": "fileToCopy.txt",
    },
    spool_list_recipient={"ReciptNoForwarding": False},
)
t1_flow.add_job(folder=f1, job=j1)

j1 = COPYJob(
    folder=f1,
    job_name="copy",
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
    post_job_action={
        "Spool": "CopyToFile",
        "SpoolFile": "spoolfile.log",
        "SpoolSaveToPDF": True,
        "JobLog": "CopyToFile",
        "JobLogFile": "Log.txt",
        "JobCompletionStatusWillDependOnApplicationStatus": True,
    },
    detect_spawned_job={
        "DetectAndCreate": "SpecificJobDefinition",
        "JobName": "Specific-Job-123",
        "StartSpawnedJob": True,
        "JobEndInControlMOnlyAftreChildJobsCompleteOnSap": True,
        "JobCompletionStatusDependsOnChildJobsStatus": True,
    },
)
t1_flow.add_job(folder=f1, job=j1)

j1 = BatchAccountJob(
    folder=f1,
    job_name="batchaccount",
    connection_profile="AZURE_CONNECTION",
    job_id="AzureJob1",
    command_line="echo Hello",
    append_log=False,
    wallclock={"Time": "770", "Unit": "Minutes"},
    max_tries={"Count": "6", "Option": "Custom"},
    retention={"Time": "1", "Unit": "Hours"},
)
t1_flow.add_job(folder=f1, job=j1)

j1 = LogicAppsJob(
    folder=f1,
    job_name="logicapps",
    connection_profile="AZURE_CONNECTION",
    logic_app_name="MyLogicApp",
    request_body={"name": "BMC"},
    append_log=False,
)
t1_flow.add_job(folder=f1, job=j1)

j1 = FunctionJob(
    folder=f1,
    job_name="function",
    connection_profile="AZURE_CONNECTION",
    append_log=False,
    function="AzureFunction",
    function_app="AzureFunctionApp",
    parameters=[
        {"firstParamName": "firstParamValue"},
        {"secondParamName": "secondParamValue"},
    ],
)
t1_flow.add_job(folder=f1, job=j1)

j1 = SqoopJob(
    folder=f1,
    job_name="sqoop",
    host="edgenode",
    connection_profile="SQOOP_CONNECTION_PROFILE",
    sqoop_command="import --table foo",
    sqoop_options=[
        {"--warehouse-dir": "/shared"},
        {"--default-character-set": "latin1"},
    ],
    sqoop_archives="",
    sqoop_files="",
    pre_commands={
        "FailJobOnCommandFailure": False,
        "Commands": [
            {"get": "hdfs://nn.example.com/user/hadoop/file localfile"},
            {"rm": "hdfs://nn.example.com/file /user/hadoop/emptydir"},
        ],
    },
    post_commands={
        "FailJobOnCommandFailure": True,
        "Commands": [{"put": "localfile hdfs://nn.example.com/user/hadoop/file"}],
    },
)
t1_flow.add_job(folder=f1, job=j1)

j1 = HDFSCommandsJob(
    folder=f1,
    job_name="hdfscommands",
    host="edgenode",
    connection_profile="DEV_CLUSTER",
    commands=[
        {"get": "hdfs://nn.example.com/user/hadoop/file localfile"},
        {"rm": "hdfs://nn.example.com/file /user/hadoop/emptydir"},
    ],
)
t1_flow.add_job(folder=f1, job=j1)

j1 = HDFSFileWatcherJob(
    folder=f1,
    job_name="hdfsfilewatcher",
    host="edgenode",
    connection_profile="DEV_CLUSTER",
    hdfs_file_path="/inputs/filename",
    min_deteced_size="1",
    max_wait_time="2",
)
t1_flow.add_job(folder=f1, job=j1)

j1 = MapredStreamingJob(
    folder=f1,
    job_name="mapredstreaming",
    host="edgenode",
    connection_profile="DEV_CLUSTER",
    input_path="/user/robot/input/*",
    output_path="/tmp/output",
    mapper_command="mapper.py",
    reducer_command="reducer.py",
    general_options=[
        {"-D": "fs.permissions.umask-mode=000"},
        {
            "-files": "/home/user/hadoop-streaming/mapper.py,/home/user/hadoop-streaming/reducer.py"
        },
    ],
)
t1_flow.add_job(folder=f1, job=j1)

j1 = DistCpJob(
    folder=f1,
    job_name="distcp",
    host="edgenode",
    connection_profile="DEV_CLUSTER",
    target_path="hdfs://nns2:8020/foo/bar",
    source_paths=["hdfs://nn1:8020/foo/a"],
)
t1_flow.add_job(folder=f1, job=j1)

j1 = HiveJob(
    folder=f1,
    job_name="hive",
    host="edgenode",
    connection_profile="HIVE_CONNECTION_PROFILE",
    hive_script="/home/user1/hive.script",
)
t1_flow.add_job(folder=f1, job=j1)

j1 = OozieJob(
    folder=f1,
    job_name="oozie",
    host="edgenode",
    connection_profile="DEV_CLUSTER",
    job_properties_file="/home/user/job.properties",
    oozie_options=[
        {"inputDir": "/usr/tucu/inputdir"},
        {"outputDir": "/usr/tucu/outputdir"},
    ],
)
t1_flow.add_job(folder=f1, job=j1)

j1 = MapReduceJob(
    folder=f1,
    job_name="mapreduce",
    host="edgenode",
    connection_profile="DEV_CLUSTER",
    program_jar="/home/user1/hadoop-jobs/hadoop-mapreduce-examples.jar",
    main_class="pi",
    arguments=["1", "2"],
    pre_commands={
        "FailJobOnCommandFailure": False,
        "Commands": [
            {"get": "hdfs://nn.example.com/user/hadoop/file localfile"},
            {"rm": "hdfs://nn.example.com/file /user/hadoop/emptydir"},
        ],
    },
    post_commands={
        "FailJobOnCommandFailure": True,
        "Commands": [{"put": "localfile hdfs://nn.example.com/user/hadoop/file"}],
    },
)
t1_flow.add_job(folder=f1, job=j1)

j1 = PigJob(
    folder=f1,
    job_name="pig",
    connection_profile="DEV_CLUSTER",
    pig_script="/home/user/script.pig",
    host="edgenode",
    parameters=[{"amount": "1000"}, {"volume": "120"}],
    pre_commands={
        "FailJobOnCommandFailure": False,
        "Commands": [
            {"get": "hdfs://nn.example.com/user/hadoop/file localfile"},
            {"rm": "hdfs://nn.example.com/file /user/hadoop/emptydir"},
        ],
    },
    post_commands={
        "FailJobOnCommandFailure": True,
        "Commands": [{"put": "localfile hdfs://nn.example.com/user/hadoop/file"}],
    },
)
t1_flow.add_job(folder=f1, job=j1)

j1 = TajoQueryJob(
    folder=f1,
    job_name="tajoquery",
    connection_profile="TAJO_CONNECTION_PROFILE",
    host="edgenode",
    open_query="SELECT %%firstParamName AS VAR1 n FROM DUMMY n ORDER BY t VAR1 DESC",
)
t1_flow.add_job(folder=f1, job=j1)

j1 = InputFileJob(
    folder=f1,
    job_name="inputfile",
    connection_profile="TAJO_CONNECTION_PROFILE",
    host="edgenode",
    full_file_path="/home/user/tajo_command.sh",
    parameters=[{"amount": "1000"}, {"volume": "120"}],
)
t1_flow.add_job(folder=f1, job=j1)

j1 = PythonJob(
    folder=f1,
    job_name="python",
    host="edgenode",
    connection_profile="DEV_CLUSTER",
    spark_script="/home/user/processData.py",
)
t1_flow.add_job(folder=f1, job=j1)

j1 = ScalaJavaJob(
    folder=f1,
    job_name="scalajava",
    host="edgenode",
    connection_profile="DEV_CLUSTER",
    program_jar="/home/user/ScalaProgram.jar",
    main_class="com.mycomp.sparkScalaProgramName.mainClassName",
    arguments=["1000", "120"],
    pre_commands={
        "FailJobOnCommandFailure": False,
        "Commands": [
            {"get": "hdfs://nn.example.com/user/hadoop/file localfile"},
            {"rm": "hdfs://nn.example.com/file /user/hadoop/emptydir"},
        ],
    },
    post_commands={
        "FailJobOnCommandFailure": True,
        "Commands": [{"put": "localfile hdfs://nn.example.com/user/hadoop/file"}],
    },
    spark_options=[{"--master": "yarn"}, {"--num": "-executors 50"}],
)
t1_flow.add_job(folder=f1, job=j1)

j1 = LambdaJob(
    folder=f1,
    job_name="lambda",
    connection_profile="AWS_CONNECTION",
    function_name="LambdaFunction",
    version="1",
    payload={"myVar": "value1", "myOtherVar": "value2"},
    append_log_to_output=True,
)
t1_flow.add_job(folder=f1, job=j1)

j1 = BatchJob(
    folder=f1,
    job_name="batch",
    connection_profile="AWS_CONNECTION",
    job_definition="jobDef1",
    job_definition_revision="3",
    job_queue="queue1",
    aws_job_type="Array",
    array_size="100",
    depends_on={"DependencyType": "Standard", "JobDependsOn": "job5"},
    command=["ffmpeg", "-i"],
    memory="10",
    v_c_p_us="2",
    job_attempts="5",
    execution_timeout="60",
    append_log_to_output=False,
)
t1_flow.add_job(folder=f1, job=j1)

j1 = StepFunctionJob(
    folder=f1,
    job_name="stepfunction",
    connection_profile="AWS_CONNECTION",
    state_machine="StateMachine1",
    execution_name="Execution1",
    input={"myVar": "value1", "myOtherVar": "value2"},
    append_log_to_output=True,
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
