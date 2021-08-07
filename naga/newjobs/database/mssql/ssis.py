from naga.jobs.base import BaseJob

class SSISJob(BaseJob):
	def __init__(self, folder, job_name, 
				connection_profile,
				package_source,
				package_name,
				config_files,
				properties,
				type = None,
				run_as = None,
				host = None,
		BaseJob.__init__(self, folder, job_name, description=description, host=host, run_as=run_as)
		self.connection_profile = connection_profile
		self.package_source = package_source
		self.package_name = package_name
		self.config_files = config_files
		self.properties = properties
		self.type = type
		self.run_as = run_as
		self.host = host

	def get_json(self):
		job_json = BaseJob.get_json(self)
		job_json['Type'] = 'Job:Database:MSSQL:SSIS'
		if self.connection_profile != None:
			job_json['ConnectionProfile'] = self.connection_profile
		if self.package_source != None:
			job_json['PackageSource'] = self.package_source
		if self.package_name != None:
			job_json['PackageName'] = self.package_name
		if self.config_files != None:
			job_json['ConfigFiles'] = self.config_files
		if self.properties != None:
			job_json['Properties'] = self.properties
		if self.type != None:
			job_json['Type'] = self.type
		if self.run_as != None:
			job_json['RunAs'] = self.run_as
		if self.host != None:
			job_json['Host'] = self.host
		return job_json
