from naga.jobs.base import BaseJob


class ScriptJob(BaseJob):
    def __init__(self, folder, job_name, file_name, file_path, host=None, run_as=None, description=None, confirm=False):
        BaseJob.__init__(self, folder, job_name, description=description, host=host, run_as=run_as)
        self.file_name = file_name
        self.file_path = file_path
        self.confirm = confirm

    def get_json(self):
        job_json = BaseJob.get_json(self)
        job_json["Type"] = "Job:Script"
        job_json["FileName"] = self.file_name
        job_json["FilePath"] = self.file_path
        job_json["Confirm"] = self.confirm
        return job_json