from naga.core.base import BaseJob

class GLUEJob(BaseJob):
	def __init__(self, folder, job_name, 
				connection_profile,
				aiglue_job_name,
				aiglue_job_arguments,
				aiarguments,
				aistatus_polling_frequency,
				host=None, run_as=None, description=None):

		BaseJob.__init__(self, folder, job_name, description=description, host=host, run_as=run_as)
		self.connection_profile = connection_profile
		self.aiglue_job_name = aiglue_job_name
		self.aiglue_job_arguments = aiglue_job_arguments
		self.aiarguments = aiarguments
		self.aistatus_polling_frequency = aistatus_polling_frequency

	def get_json(self):
		job_json = BaseJob.get_json(self)
		job_json['Type'] = 'Job:GLUE'
		if self.connection_profile != None:
			job_json['ConnectionProfile'] = self.connection_profile
		if self.aiglue_job_name != None:
			job_json['AI-Glue Job Name'] = self.aiglue_job_name
		if self.aiglue_job_arguments != None:
			job_json['AI-Glue Job Arguments'] = self.aiglue_job_arguments
		if self.aiarguments != None:
			job_json['AI-Arguments'] = self.aiarguments
		if self.aistatus_polling_frequency != None:
			job_json['AI-Status Polling Frequency'] = self.aistatus_polling_frequency
		return job_json
