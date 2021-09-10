from ctm_python_client.core.base import BaseJob


class ADFJob(BaseJob):
    def __init__(
        self,
        folder,
        job_name,
        connection_profile,
        airesource_group_name,
        aidata_factory_name,
        aipipeline_name,
        aiparameters,
        aistatus_polling_frequency,
        host=None,
        run_as=None,
        description=None,
    ):

        BaseJob.__init__(
            self, folder, job_name, description=description, host=host, run_as=run_as
        )
        self.connection_profile = connection_profile
        self.airesource_group_name = airesource_group_name
        self.aidata_factory_name = aidata_factory_name
        self.aipipeline_name = aipipeline_name
        self.aiparameters = aiparameters
        self.aistatus_polling_frequency = aistatus_polling_frequency

    def get_json(self):
        job_json = BaseJob.get_json(self)
        job_json["Type"] = "Job:ADF"
        if self.connection_profile != None:
            job_json["ConnectionProfile"] = self.connection_profile
        if self.airesource_group_name != None:
            job_json["AI-Resource Group Name"] = self.airesource_group_name
        if self.aidata_factory_name != None:
            job_json["AI-Data Factory Name"] = self.aidata_factory_name
        if self.aipipeline_name != None:
            job_json["AI-Pipeline Name"] = self.aipipeline_name
        if self.aiparameters != None:
            job_json["AI-Parameters"] = self.aiparameters
        if self.aistatus_polling_frequency != None:
            job_json["AI-Status Polling Frequency"] = self.aistatus_polling_frequency
        return job_json
