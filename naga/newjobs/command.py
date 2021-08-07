from naga.jobs.base import BaseJob

class CommandJob(BaseJob):
	def __init__(self, folder, job_name, 
				created_by,
				command,
				events_to_add,
				type = None,
				run_as = None,
				host = None,
		BaseJob.__init__(self, folder, job_name, description=description, host=host, run_as=run_as)
		self.created_by = created_by
		self.command = command
		self.events_to_add = events_to_add
		self.type = type
		self.run_as = run_as
		self.host = host

	def get_json(self):
		job_json = BaseJob.get_json(self)
		job_json['Type'] = 'Job:Command'
		if self.created_by != None:
			job_json['CreatedBy'] = self.created_by
		if self.command != None:
			job_json['Command'] = self.command
		if self.events_to_add != None:
			job_json['eventsToAdd'] = self.events_to_add
		if self.type != None:
			job_json['Type'] = self.type
		if self.run_as != None:
			job_json['RunAs'] = self.run_as
		if self.host != None:
			job_json['Host'] = self.host
		return job_json
