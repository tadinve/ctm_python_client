from naga.jobs.base import BaseJob


class AIAirflowCLI(BaseJob):
    def __init__(
        self, folder, job_name, connection_profile, ai_action, ai_dag_id, host=None, run_as=None, description=None
    ):
        BaseJob.__init__(self, folder, job_name, description, host, run_as)
        self.connection_profile = connection_profile
        self.ai_action = ai_action
        self.ai_dag_id = ai_dag_id

    def get_json(self):
        job_json = BaseJob.get_json(self)
        job_json["Type"] = "Job:ApplicationIntegrator:AI AirflowCLI"
        job_json["ConnectionProfile"] = self.connection_profile
        job_json["AI-Action"] = self.ai_action
        job_json["AI-DAG_ID"] = self.ai_dag_id
        return job_json

class AI_Asps(BaseJob):
    def __init__(
            self, folder, job_name, connection_profile, ai_action, ai_aapi_endpoint_url,
            ai_aapi_token_value, ai_agent_token_tag, ai_customer_code,
            host=None, run_as=None, description=None):

        BaseJob.__init__(self, folder, job_name, description, host, run_as)
        self.connection_profile = connection_profile
        self.ai_action = ai_action
        self.ai_aapi_endpoint_url = ai_aapi_endpoint_url
        self.ai_aapi_token_value = ai_aapi_token_value
        self.ai_agent_token_tag = ai_agent_token_tag
        self.ai_customer_code = ai_customer_code
    
    def get_json(self):
        job_json = BaseJob.get_json(self)
        job_json["Type"] = "Job:ApplicationIntegrator:AI ASPS"
        job_json["ConnectionProfile"] = self.connection_profile
        job_json["AI-Action"] = self.ai_action
        job_json['AI-AAPI Endpoint URL'] = self.ai_aapi_endpoint_url	
        job_json['AI-AAPI Token Value'] = self.ai_aapi_token_value	
        job_json['AI-Agent Token Tag'] = self.ai_agent_token_tag	
        job_json['AI-Customer Code'] = self.ai_customer_code	
        return job_json



class AIBlobStorage(BaseJob):
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
        BaseJob.__init__(self, folder, job_name, description, host, run_as)
        self.connection_profile = connection_profile
        self.ai_action = ai_action
        self.ai_blob_name = ai_blob_name
        self.ai_container = ai_container
        self.ai_file_path = ai_file_path
        self.ai_public_access = ai_public_access

    def get_json(self):
        job_json = BaseJob.get_json(self)

        job_json["Type"] = "Job:ApplicationIntegrator:AI Blob Storage"
        job_json["ConnectionProfile"] = self.connection_profile
        job_json["AI-Action"] = self.ai_action
        job_json["AI-Blob name (Up/Download)"] = self.ai_blob_name
        job_json["AI-Container (Up/Download)"] = self.ai_container
        job_json["AI-File path"] = self.ai_file_path
        job_json["AI-Public Access"] = self.ai_public_access

        return job_json
