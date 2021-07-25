from naga.jobs.base import BaseJob


class InformaticaJob(BaseJob):
    def __init__(self, folder, job_name, connection_profile, repository_folder, workflow, 
                workflow_execution_mode, workflow_restart_mode, enable_output, enable_error_details,
                priority, host=None, run_as=None, description=None):
        BaseJob.__init__(self, folder, job_name, description, host, run_as)
        self.connection_profile = connection_profile
        self.repository_folder = repository_folder
        self.workflow = workflow
        self.workflow_execution_mode = workflow_execution_mode
        self.workflow_restart_mode = workflow_restart_mode
        self.enable_output = enable_output
        self.enable_error_details = enable_error_details
        self.priority = priority

    def get_json(self):
        job_json = BaseJob.get_json(self)
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