from naga.jobs.base import BaseJob

class DummyJob(BaseJob):
    def __init__(self, folder, job_name):
        BaseJob.__init__(self, folder, job_name)

    def get_json(self):
        job_json = BaseJob.get_json(self)
        job_json["Type"] = "Job:Dummy"
        return job_json