from ctm_python_client.core.base import BaseJob


class AIMonitorRemoteJob(BaseJob):
    def __init__(
        self,
        folder,
        job_name,
        connection_profile,
        aihost,
        aiport,
        aiuser_name,
        aipassword,
        airemote_jobto_monitor,
        host=None,
        run_as=None,
        description=None,
    ):

        BaseJob.__init__(
            self, folder, job_name, description=description, host=host, run_as=run_as
        )
        self.connection_profile = connection_profile
        self.aihost = aihost
        self.aiport = aiport
        self.aiuser_name = aiuser_name
        self.aipassword = aipassword
        self.airemote_jobto_monitor = airemote_jobto_monitor

    def get_json(self):
        job_json = BaseJob.get_json(self)
        job_json["Type"] = "Job:ApplicationIntegrator:AI Monitor Remote Job"
        if self.connection_profile != None:
            job_json["ConnectionProfile"] = self.connection_profile
        if self.aihost != None:
            job_json["AI-Host"] = self.aihost
        if self.aiport != None:
            job_json["AI-Port"] = self.aiport
        if self.aiuser_name != None:
            job_json["AI-User Name"] = self.aiuser_name
        if self.aipassword != None:
            job_json["AI-Password"] = self.aipassword
        if self.airemote_jobto_monitor != None:
            job_json["AI-Remote Job to Monitor"] = self.airemote_jobto_monitor
        return job_json
