class CmBaseJob:
    """
    Abstract class to be derived for jobs. Jobs are processing items with state
    and duration that aren't task instances. For instance a CommandJob is
    a collection of task instance runs, but should have its own state, start
    and end time.
    """

    def __init__(self, folder, job_name, description=None, host=None, run_as=None):
        self.folder = folder
        self.job_name = job_name
        self.host = host
        self.run_as = run_as
        self.capture_count = 0
        self.job_json = {"Type": None}  # This will be overriden in the inhereted class. S
        self.description = description
        if self.host is not None:
            self.job_json["Host"] = self.host
        if self.run_as is not None:
            self.job_json["RunAs"] = self.run_as
        if self.description is not None:
            self.job_json["Description"] = self.description

    def get_job_name(self):
        return self.job_name

    def get_folder(self):
        return self.folder

    def get_json(self):
        return self.job_json

    def on_success_send_mail(self, mail_subject, mail_to, mail_message):
        self.job_json["OnSuccessMail"] = {
            "Type": "If:CompletionStatus",
            "CompletionStatus": "OK",
            "Mail_0": {"Type": "Action:Mail", "Subject": mail_subject, "To": mail_to, "Message": mail_message},
        }

    def capture_output(self, variable, capture_type, search_string):
        self.capture_count += 1
        self.job_json["CaptureOutput_" + str(self.capture_count)] = {
            "Type": "Action:CaptureOutput",
            "Capture": capture_type,
            "Search": search_string,
            "VariableName": "\\\\" + variable,
            "ForwardBy": {"ColumnsOption": "Characters"},
        }

    def set_job_schedule(self, months=None, month_days=None, week_days=None, from_time=None, to_time=None):
        self.job_json["When"] = {}
        if months is not None:
            self.job_json["When"]["Months"] = months
        if month_days is not None:
            self.job_json["When"]["MonthDays"] = month_days
        if week_days is not None:
            self.job_json["When"]["WeekDays"] = week_days
        if from_time is not None:
            self.job_json["When"]["FromTime"] = from_time
        if to_time is not None:
            self.job_json["When"]["ToTime"] = to_time

class CmDummyJob(CmBaseJob):
    def __init__(self, folder, job_name):
        CmBaseJob.__init__(self, folder, job_name)

    def get_json(self):
        job_json = CmBaseJob.get_json(self)
        job_json["Type"] = "Job:Dummy"
        return job_json


class CmCommandJob(CmBaseJob):
    def __init__(self, folder, job_name, command, pre_command=None, host=None, run_as=None, description=None):
        CmBaseJob.__init__(self, folder, job_name, description=description, host=host, run_as=run_as)
        self.command = command
        self.pre_command = pre_command

    def get_json(self):
        job_json = CmBaseJob.get_json(self)
        job_json["Type"] = "Job:Command"
        job_json["Command"] = self.command
        if self.pre_command is not None:
            job_json["PreCommand"] = self.pre_command

        return job_json


class CmScriptJob(CmBaseJob):
    def __init__(self, folder, job_name, file_name, file_path, host=None, run_as=None, description=None, confirm=False):
        CmBaseJob.__init__(self, folder, job_name, description=description, host=host, run_as=run_as)
        self.file_name = file_name
        self.file_path = file_path
        self.confirm = confirm

    def get_json(self):
        job_json = CmBaseJob.get_json(self)
        job_json["Type"] = "Job:Script"
        job_json["FileName"] = self.file_name
        job_json["FilePath"] = self.file_path
        job_json["Confirm"] = self.confirm
        return job_json


class CmEmbeddedScript(CmBaseJob):
    def __init__(self, folder, job_name, script, filename, host=None, run_as=None, description=None):
        CmBaseJob.__init__(self, folder, job_name, description, host, run_as)
        self.script = script
        self.filename = filename

    def get_json(self):
        job_json = CmBaseJob.get_json(self)
        job_json["Type"] = "Job:EmbeddedScript"
        job_json["Script"] = self.script
        job_json["FileName"] = self.filename
        return job_json


class CmDatabaseSQLScript(CmBaseJob):
    def __init__(
        self,
        folder,
        job_name,
        sql_script,
        connection_profile,
        output_sql="Y",
        output_format="CSV",
        host=None,
        run_as=None,
        description=None,
    ):
        CmBaseJob.__init__(self, folder, job_name, description, host, run_as)
        self.connection_profile = connection_profile
        self.sql_script = sql_script
        self.output_sql = output_sql
        self.output_format = output_format
        self.sql_script = sql_script

    def get_json(self):
        job_json = CmBaseJob.get_json(self)
        job_json["Type"] = "Job:Database:SQLScript"
        job_json["ConnectionProfile"] = self.connection_profile
        job_json["SQLScript"] = self.sql_script
        job_json["OutputSQLOutput"] = self.output_sql
        job_json["SQLOutputFormat"] = self.output_format
        return job_json


class CmFileTransferJob(CmBaseJob):
    def __init__(self, folder, job_name, connection_src, connection_dest, host=None, run_as=None, description=None):
        CmBaseJob.__init__(self, folder, job_name, description, host, run_as)
        self.connection_src = connection_src
        self.connection_dest = connection_dest
        self.transfers = []

    def add_file_transfer(self, src, dest, option, transfer_type=None):
        transfer = {"Src": src,
                    "Dest": dest,
                    "TransferOption": option}
        if transfer_type is not None:
            transfer["TransferType"] = transfer_type
        self.transfers.append(transfer)

    def get_json(self):
        job_json = CmBaseJob.get_json(self)
        job_json["Type"] = "Job:FileTransfer"
        job_json["ConnectionProfileSrc"] = self.connection_src
        job_json["ConnectionProfileDest"] = self.connection_dest
        job_json["FileTransfers"] = self.transfers
        return job_json


class CmHDFSCommands(CmBaseJob):
    def __init__(self, folder, job_name, connection_profile, commands, host=None, run_as=None, description=None):
        CmBaseJob.__init__(self, folder, job_name, description, host, run_as)
        self.connection_profile = connection_profile
        self.commands = commands

    def get_json(self):
        job_json = CmBaseJob.get_json(self)
        job_json["Type"] = "Job:Hadoop:HDFSCommands"
        job_json["ConnectionProfile"] = self.connection_profile
        job_json["Commands"] = self.commands
        return job_json


class CmSparkScalaJava(CmBaseJob):
    def __init__(
        self,
        folder,
        job_name,
        connection_profile,
        program_jar,
        main_class,
        arguments,
        pre_commands,
        output,
        host=None,
        run_as=None,
        description=None,
    ):
        CmBaseJob.__init__(self, folder, job_name, description, host, run_as)
        self.connection_profile = connection_profile
        self.program_jar = program_jar
        self.main_class = main_class
        self.arguments = arguments
        self.output = output
        self.pre_commands = pre_commands

    def get_json(self):
        job_json = CmBaseJob.get_json(self)
        job_json["Type"] = "Job:Hadoop:Spark:ScalaJava"
        job_json["ConnectionProfile"] = self.connection_profile
        job_json["ProgramJar"] = self.program_jar
        job_json["MainClass"] = self.main_class
        job_json["Arguments"] = self.arguments
        job_json["PreCommands"] = self.pre_commands
        job_json["Output"] = self.output
        return job_json


class CmDatabaseEmbeddedQuery(CmBaseJob):
    def __init__(self, folder, job_name, query, connection_profile, host=None, run_as=None, description=None):
        CmBaseJob.__init__(self, folder, job_name, description, host, run_as)
        self.connection_profile = connection_profile
        self.query = query

    def get_json(self):
        job_json = CmBaseJob.get_json(self)
        job_json["Type"] = "Job:Database:EmbeddedQuery"
        job_json["ConnectionProfile"] = self.connection_profile
        job_json["Query"] = self.query
        return job_json


class CmAIAirflowCLI(CmBaseJob):
    def __init__(
        self, folder, job_name, connection_profile, ai_action, ai_dag_id, host=None, run_as=None, description=None
    ):
        CmBaseJob.__init__(self, folder, job_name, description, host, run_as)
        self.connection_profile = connection_profile
        self.ai_action = ai_action
        self.ai_dag_id = ai_dag_id

    def get_json(self):
        job_json = CmBaseJob.get_json(self)
        job_json["Type"] = "Job:ApplicationIntegrator:AI AirflowCLI"
        job_json["ConnectionProfile"] = self.connection_profile
        job_json["AI-Action"] = self.ai_action
        job_json["AI-DAG_ID"] = self.ai_dag_id
        return job_json

class CmAI_Asps(CmBaseJob):
    def __init__(
            self, folder, job_name, connection_profile, ai_action, ai_aapi_endpoint_url,
            ai_aapi_token_value, ai_agent_token_tag, ai_customer_code,
            host=None, run_as=None, description=None):

        CmBaseJob.__init__(self, folder, job_name, description, host, run_as)
        self.connection_profile = connection_profile
        self.ai_action = ai_action
        self.ai_aapi_endpoint_url = ai_aapi_endpoint_url
        self.ai_aapi_token_value = ai_aapi_token_value
        self.ai_agent_token_tag = ai_agent_token_tag
        self.ai_customer_code = ai_customer_code
    
    def get_json(self):
        job_json = CmBaseJob.get_json(self)
        job_json["Type"] = "Job:ApplicationIntegrator:AI ASPS"
        job_json["ConnectionProfile"] = self.connection_profile
        job_json["AI-Action"] = self.ai_action
        job_json['AI-AAPI Endpoint URL'] = self.ai_aapi_endpoint_url	
        job_json['AI-AAPI Token Value'] = self.ai_aapi_token_value	
        job_json['AI-Agent Token Tag'] = self.ai_agent_token_tag	
        job_json['AI-Customer Code'] = self.ai_customer_code	
        return job_json

class CmInformaticaJob(CmBaseJob):
    def __init__(self, folder, job_name, connection_profile, repository_folder, workflow, 
                workflow_execution_mode, workflow_restart_mode, enable_output, enable_error_details,
                priority, host=None, run_as=None, description=None):
        CmBaseJob.__init__(self, folder, job_name, description, host, run_as)
        self.connection_profile = connection_profile
        self.repository_folder = repository_folder
        self.workflow = workflow
        self.workflow_execution_mode = workflow_execution_mode
        self.workflow_restart_mode = workflow_restart_mode
        self.enable_output = enable_output
        self.enable_error_details = enable_error_details
        self.priority = priority

    def get_json(self):
        job_json = CmBaseJob.get_json(self)
        job_json["Type"] = "Job:Informatica"
        job_json['ConnectionProfile'] = self.connection_profile
        job_json['RepositoryFolder'] = self.repository_folder
        job_json['Workflow'] = self.workflow
        job_json['WorkflowExecutionMode'] = self.workflow_execution_mode
        job_json['WorkflowRestartMode'] = self.workflow_restart_mode
        job_json['EnableOutput'] = self.enable_output
        job_json['EnableErrorDetails'] = self.enable_error_details
        job_json['Priority'] = self.priority
        return job_json

class CmAIBlobStorage(CmBaseJob):
    def __init__(
        self,
        folder,
        job_name,
        connection_profile,
        ai_action,
        ai_blob_name,
        ai_container,
        ai_file_path,
        ai_public_access,
        host=None,
        run_as=None,
        description=None,
    ):
        CmBaseJob.__init__(self, folder, job_name, description, host, run_as)
        self.connection_profile = connection_profile
        self.ai_action = ai_action
        self.ai_blob_name = ai_blob_name
        self.ai_container = ai_container
        self.ai_file_path = ai_file_path
        self.ai_public_access = ai_public_access

    def get_json(self):
        job_json = CmBaseJob.get_json(self)

        job_json["Type"] = "Job:ApplicationIntegrator:AI Blob Storage"
        job_json["ConnectionProfile"] = self.connection_profile
        job_json["AI-Action"] = self.ai_action
        job_json["AI-Blob name (Up/Download)"] = self.ai_blob_name
        job_json["AI-Container (Up/Download)"] = self.ai_container
        job_json["AI-File path"] = self.ai_file_path
        job_json["AI-Public Access"] = self.ai_public_access

        return job_json
