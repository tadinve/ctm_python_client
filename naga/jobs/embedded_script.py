from naga.jobs.base import BaseJob

class EmbeddedScriptJob(BaseJob):
    def __init__(self, folder, job_name, script, filename, host=None, run_as=None, description=None):
        BaseJob.__init__(self, folder, job_name, description, host, run_as)
        self.script = script
        self.filename = filename

    def get_json(self):
        job_json = BaseJob.get_json(self)
        job_json["Type"] = "Job:EmbeddedScript"
        job_json["Script"] = self.script
        job_json["FileName"] = self.filename
        return job_json
