from naga.jobs.base import BaseJob

class GLUEJob(BaseJob):
	def __init__(self, folder, job_name, 
				connection_profile,
				ai_glue_job_name,
				ai_glue_job_arguments,
				ai_arguments,
				ai_status_polling_frequency,
			host=None, run_as=None, description=None):
		BaseJob.__init__(self, folder, job_name, description=description, host=host, run_as=run_as)
		self.connection_profile = connection_profile
		self.ai_glue_job_name = ai_glue_job_name
		self.ai_glue_job_arguments = ai_glue_job_arguments
		self.ai_arguments = ai_arguments
		self.ai_status_polling_frequency = ai_status_polling_frequency

	def get_json(self):
		job_json = BaseJob.get_json(self)
		job_json['Type'] = 'Job:GLUE'
		if self.connection_profile != None:
			job_json['ConnectionProfile'] = self.connection_profile
		if self.ai_glue_job_name != None:
			job_json['AI-Glue Job Name'] = self.ai_glue_job_name
		if self.ai_glue_job_arguments != None:
			job_json['AI-Glue Job Arguments'] = self.ai_glue_job_arguments
		if self.ai_arguments != None:
			job_json['AI-Arguments'] = self.ai_arguments
		if self.ai_status_polling_frequency != None:
			job_json['AI-Status Polling Frequency'] = self.ai_status_polling_frequency
		return job_json
