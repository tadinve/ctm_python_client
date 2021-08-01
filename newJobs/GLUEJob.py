from naga.jobs.base import BaseJob

class GLUEJob(BaseJob):
	def __init__(self, folder, job_name, 
				connection_profile,
				a_i_glue_job_name,
				a_i_glue_job_arguments,
				a_i_arguments,
				a_i_status_polling_frequency,
			host=None, run_as=None, description=None):
		BaseJob.__init__(self, folder, job_name, description=description, host=host, run_as=run_as)
		self.connection_profile = connection_profile
		self.a_i_glue_job_name = a_i_glue_job_name
		self.a_i_glue_job_arguments = a_i_glue_job_arguments
		self.a_i_arguments = a_i_arguments
		self.a_i_status_polling_frequency = a_i_status_polling_frequency

	def get_json(self):
		job_json = BaseJob.get_json(self)
		job_json['Type'] = 'Job:GLUE'
		if self.connection_profile != None:
			job_json['ConnectionProfile'] = self.connection_profile
		if self.a_i_glue_job_name != None:
			job_json['AI-Glue Job Name'] = self.a_i_glue_job_name
		if self.a_i_glue_job_arguments != None:
			job_json['AI-Glue Job Arguments'] = self.a_i_glue_job_arguments
		if self.a_i_arguments != None:
			job_json['AI-Arguments'] = self.a_i_arguments
		if self.a_i_status_polling_frequency != None:
			job_json['AI-Status Polling Frequency'] = self.a_i_status_polling_frequency
		return job_json
