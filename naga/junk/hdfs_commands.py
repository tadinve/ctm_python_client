from naga.jobs.base import BaseJob


class HDFSCommandsJob(BaseJob):

    def __init__(self, folder, job_name, connection_profile, commands, host=None, run_as=None, description=None):
        BaseJob.__init__(self, folder, job_name, description, host, run_as)
        self.connection_profile = connection_profile
        self.commands = commands

    def get_json(self):
        job_json = BaseJob.get_json(self)
        job_json["Type"] = "Job:Hadoop:HDFSCommands"
        job_json["ConnectionProfile"] = self.connection_profile
        job_json["Commands"] = self.commands
        return job_json