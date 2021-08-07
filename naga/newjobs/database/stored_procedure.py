from naga.jobs.base import BaseJob

class StoredProcedureJob(BaseJob):
	def __init__(self, folder, job_name, 
				stored_procedure,
				parameters,
				return_value,
				schema,
				connection_profile,
				type = None,
				run_as = None,
				host = None,
		BaseJob.__init__(self, folder, job_name, description=description, host=host, run_as=run_as)
		self.stored_procedure = stored_procedure
		self.parameters = parameters
		self.return_value = return_value
		self.schema = schema
		self.connection_profile = connection_profile
		self.type = type
		self.run_as = run_as
		self.host = host

	def get_json(self):
		job_json = BaseJob.get_json(self)
		job_json['Type'] = 'Job:Database:StoredProcedure'
		if self.stored_procedure != None:
			job_json['StoredProcedure'] = self.stored_procedure
		if self.parameters != None:
			job_json['Parameters'] = self.parameters
		if self.return_value != None:
			job_json['ReturnValue'] = self.return_value
		if self.schema != None:
			job_json['Schema'] = self.schema
		if self.connection_profile != None:
			job_json['ConnectionProfile'] = self.connection_profile
		if self.type != None:
			job_json['Type'] = self.type
		if self.run_as != None:
			job_json['RunAs'] = self.run_as
		if self.host != None:
			job_json['Host'] = self.host
		return job_json
