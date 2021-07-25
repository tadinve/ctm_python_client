from naga.jobs.base import BaseJob



class DatabaseSQLScriptJob(BaseJob):
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
        BaseJob.__init__(self, folder, job_name, description, host, run_as)
        self.connection_profile = connection_profile
        self.sql_script = sql_script
        self.output_sql = output_sql
        self.output_format = output_format
        self.sql_script = sql_script

    def get_json(self):
        job_json = BaseJob.get_json(self)
        job_json["Type"] = "Job:Database:SQLScript"
        job_json["ConnectionProfile"] = self.connection_profile
        job_json["SQLScript"] = self.sql_script
        job_json["OutputSQLOutput"] = self.output_sql
        job_json["SQLOutputFormat"] = self.output_format
        return job_json