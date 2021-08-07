from naga.jobs.base import BaseJob

class OozieJob(BaseJob):
	def __init__(self, folder, job_name, 
				connection_profile,
				job_properties_file,
				oozie_options,
				type = None,
				run_as = None,
				host = None,
		BaseJob.__init__(self, folder, job_name, description=description, host=host, run_as=run_as)
		self.connection_profile = connection_profile
		self.job_properties_file = job_properties_file
		self.oozie_options = oozie_options
		self.type = type
		self.run_as = run_as
		self.host = host

	def get_json(self):
		job_json = BaseJob.get_json(self)
		job_json['Type'] = 'Job:Hadoop:Oozie'
		if self.connection_profile != None:
			job_json['ConnectionProfile'] = self.connection_profile
		if self.job_properties_file != None:
			job_json['JobPropertiesFile'] = self.job_properties_file
		if self.oozie_options != None:
			job_json['OozieOptions'] = self.oozie_options
		if self.type != None:
			job_json['Type'] = self.type
		if self.run_as != None:
			job_json['RunAs'] = self.run_as
		if self.host != None:
			job_json['Host'] = self.host
		return job_json
