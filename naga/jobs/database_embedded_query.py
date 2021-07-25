from naga.jobs.base import BaseJob


class DatabaseEmbeddedQueryJob(BaseJob):
    def __init__(self, folder, job_name, query, connection_profile, host=None, run_as=None, description=None):
        BaseJob.__init__(self, folder, job_name, description, host, run_as)
        self.connection_profile = connection_profile
        self.query = query

    def get_json(self):
        job_json = BaseJob.get_json(self)
        job_json["Type"] = "Job:Database:EmbeddedQuery"
        job_json["ConnectionProfile"] = self.connection_profile
        job_json["Query"] = self.query
        return job_json