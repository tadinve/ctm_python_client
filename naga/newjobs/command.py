from naga.jobs.base import BaseJob

class CommandJob(BaseJob):
	def __init__(self, folder, job_name, 
				command,
				events_to_add = None,
				created_by = None,
				host=None, run_as=None, description=None):

		BaseJob.__init__(self, folder, job_name, description=description, host=host, run_as=run_as)
		self.command = command
		self.events_to_add = events_to_add
		self.created_by = created_by

	def get_json(self):
		job_json = BaseJob.get_json(self)
		job_json['Type'] = 'Job:Command'
		if self.command != None:
			job_json['Command'] = self.command
		if self.events_to_add != None:
			job_json['eventsToAdd'] = self.events_to_add
		if self.created_by != None:
			job_json['CreatedBy'] = self.created_by
		return job_json
