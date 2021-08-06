from naga.jobs.base import BaseJob

class AIMonitorRemoteJob(BaseJob):
	def __init__(self, folder, job_name, 
				connection_profile,
				ai_host,
				ai_port,
				ai_user_name,
				ai_password,
				ai_remote_jobto_monitor,
			host=None, run_as=None, description=None):
		BaseJob.__init__(self, folder, job_name, description=description, host=host, run_as=run_as)
		self.connection_profile = connection_profile
		self.ai_host = ai_host
		self.ai_port = ai_port
		self.ai_user_name = ai_user_name
		self.ai_password = ai_password
		self.ai_remote_jobto_monitor = ai_remote_jobto_monitor

	def get_json(self):
		job_json = BaseJob.get_json(self)
		job_json['Type'] = 'Job:ApplicationIntegrator:AI Monitor Remote Job'
		if self.connection_profile != None:
			job_json['ConnectionProfile'] = self.connection_profile
		if self.ai_host != None:
			job_json['AI-Host'] = self.ai_host
		if self.ai_port != None:
			job_json['AI-Port'] = self.ai_port
		if self.ai_user_name != None:
			job_json['AI-User Name'] = self.ai_user_name
		if self.ai_password != None:
			job_json['AI-Password'] = self.ai_password
		if self.ai_remote_jobto_monitor != None:
			job_json['AI-Remote Job to Monitor'] = self.ai_remote_jobto_monitor
		return job_json
