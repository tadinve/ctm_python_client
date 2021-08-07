from naga.jobs.base import BaseJob

class SQLScriptJob(BaseJob):
	def __init__(self, folder, job_name, 
				sql_script,
				connection_profile,
				parameters,
				type = None,
				run_as = None,
				host = None,
		BaseJob.__init__(self, folder, job_name, description=description, host=host, run_as=run_as)
		self.sql_script = sql_script
		self.connection_profile = connection_profile
		self.parameters = parameters
		self.type = type
		self.run_as = run_as
		self.host = host

	def get_json(self):
		job_json = BaseJob.get_json(self)
		job_json['Type'] = 'Job:Database:SQLScript'
		if self.sql_script != None:
			job_json['SQLScript'] = self.sql_script
		if self.connection_profile != None:
			job_json['ConnectionProfile'] = self.connection_profile
		if self.parameters != None:
			job_json['Parameters'] = self.parameters
		if self.type != None:
			job_json['Type'] = self.type
		if self.run_as != None:
			job_json['RunAs'] = self.run_as
		if self.host != None:
			job_json['Host'] = self.host
		return job_json
