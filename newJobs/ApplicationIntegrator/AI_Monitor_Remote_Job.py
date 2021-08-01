from naga.jobs.base import BaseJob

class AI_Monitor_Remote_Job(BaseJob):
	def __init__(self, folder, job_name, 
				connection_profile,
				a_i_host,
				a_i_port,
				a_i_user_name,
				a_i_password,
				a_i_remote_jobto_monitor,
			host=None, run_as=None, description=None):
		BaseJob.__init__(self, folder, job_name, description=description, host=host, run_as=run_as)
		self.connection_profile = connection_profile
		self.a_i_host = a_i_host
		self.a_i_port = a_i_port
		self.a_i_user_name = a_i_user_name
		self.a_i_password = a_i_password
		self.a_i_remote_jobto_monitor = a_i_remote_jobto_monitor

	def get_json(self):
		job_json = BaseJob.get_json(self)
		job_json['Type'] = 'Job:ApplicationIntegrator:AI Monitor Remote Job'
		if self.connection_profile != None:
			job_json['ConnectionProfile'] = self.connection_profile
		if self.a_i_host != None:
			job_json['AI-Host'] = self.a_i_host
		if self.a_i_port != None:
			job_json['AI-Port'] = self.a_i_port
		if self.a_i_user_name != None:
			job_json['AI-User Name'] = self.a_i_user_name
		if self.a_i_password != None:
			job_json['AI-Password'] = self.a_i_password
		if self.a_i_remote_jobto_monitor != None:
			job_json['AI-Remote Job to Monitor'] = self.a_i_remote_jobto_monitor
		return job_json
