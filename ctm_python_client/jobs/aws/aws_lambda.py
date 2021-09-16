from ctm_python_client.core.base import BaseJob


class LambdaJob(BaseJob):
    def __init__(
        self,
        folder,
        job_name,
        connection_profile,
        function_name,
        version,
        payload,
        append_log_to_output,
        host=None,
        run_as=None,
        description=None,
    ):

        BaseJob.__init__(
            self, folder, job_name, description=description, host=host, run_as=run_as
        )
        self.connection_profile = connection_profile
        self.function_name = function_name
        self.version = version
        self.payload = payload
        self.append_log_to_output = append_log_to_output

    def get_json(self):
        job_json = BaseJob.get_json(self)
        job_json["Type"] = "Job:AWS:Lambda"
        if self.connection_profile != None:
            job_json["ConnectionProfile"] = self.connection_profile
        if self.function_name != None:
            job_json["FunctionName"] = self.function_name
        if self.version != None:
            job_json["Version"] = self.version
        if self.payload != None:
            job_json["Payload"] = self.payload
        if self.append_log_to_output != None:
            job_json["AppendLogToOutput"] = self.append_log_to_output
        return job_json
