from naga.jobs.base import BaseJob

class ADFJob(BaseJob):
	def __init__(self, folder, job_name, 
				connection_profile,
				a_i_resource_group_name,
				a_i_data_factory_name,
				a_i_pipeline_name,
				a_i_parameters,
				a_i_status_polling_frequency,
			host=None, run_as=None, description=None):
		BaseJob.__init__(self, folder, job_name, description=description, host=host, run_as=run_as)
		self.connection_profile = connection_profile
		self.a_i_resource_group_name = a_i_resource_group_name
		self.a_i_data_factory_name = a_i_data_factory_name
		self.a_i_pipeline_name = a_i_pipeline_name
		self.a_i_parameters = a_i_parameters
		self.a_i_status_polling_frequency = a_i_status_polling_frequency

	def get_json(self):
		job_json = BaseJob.get_json(self)
		job_json['Type'] = 'Job:ADF'
		if self.connection_profile != None:
			job_json['ConnectionProfile'] = self.connection_profile
		if self.a_i_resource_group_name != None:
			job_json['AI-Resource Group Name'] = self.a_i_resource_group_name
		if self.a_i_data_factory_name != None:
			job_json['AI-Data Factory Name'] = self.a_i_data_factory_name
		if self.a_i_pipeline_name != None:
			job_json['AI-Pipeline Name'] = self.a_i_pipeline_name
		if self.a_i_parameters != None:
			job_json['AI-Parameters'] = self.a_i_parameters
		if self.a_i_status_polling_frequency != None:
			job_json['AI-Status Polling Frequency'] = self.a_i_status_polling_frequency
		return job_json
