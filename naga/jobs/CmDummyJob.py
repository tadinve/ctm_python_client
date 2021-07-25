from naga.jobs.CmBaseJob import CmBaseJob

class CmDummyJob(CmBaseJob):
    def __init__(self, folder, job_name):
        CmBaseJob.__init__(self, folder, job_name)

    def get_json(self):
        job_json = CmBaseJob.get_json(self)
        job_json["Type"] = "Job:Dummy"
        return job_json