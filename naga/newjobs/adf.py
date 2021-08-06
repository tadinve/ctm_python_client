from naga.jobs.base import BaseJob

class ADFJob(BaseJob):
	def __init__(self, folder, job_name, 
				connection_profile,
				ai_resource_group_name,
				ai_data_factory_name,
				ai_pipeline_name,
				ai_parameters,
				ai_status_polling_frequency,
			host=None, run_as=None, description=None):
		BaseJob.__init__(self, folder, job_name, description=description, host=host, run_as=run_as)
		self.connection_profile = connection_profile
		self.ai_resource_group_name = ai_resource_group_name
		self.ai_data_factory_name = ai_data_factory_name
		self.ai_pipeline_name = ai_pipeline_name
		self.ai_parameters = ai_parameters
		self.ai_status_polling_frequency = ai_status_polling_frequency

	def get_json(self):
		job_json = BaseJob.get_json(self)
		job_json['Type'] = 'Job:ADF'
		if self.connection_profile != None:
			job_json['ConnectionProfile'] = self.connection_profile
		if self.ai_resource_group_name != None:
			job_json['AI-Resource Group Name'] = self.ai_resource_group_name
		if self.ai_data_factory_name != None:
			job_json['AI-Data Factory Name'] = self.ai_data_factory_name
		if self.ai_pipeline_name != None:
			job_json['AI-Pipeline Name'] = self.ai_pipeline_name
		if self.ai_parameters != None:
			job_json['AI-Parameters'] = self.ai_parameters
		if self.ai_status_polling_frequency != None:
			job_json['AI-Status Polling Frequency'] = self.ai_status_polling_frequency
		return job_json
