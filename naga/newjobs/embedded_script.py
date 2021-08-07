from naga.jobs.base import BaseJob

class EmbeddedScriptJob(BaseJob):
	def __init__(self, folder, job_name, 
				script,
				file_name,
				pre_command = None,
				post_command = None,
				host=None, run_as=None, description=None):

		BaseJob.__init__(self, folder, job_name, description=description, host=host, run_as=run_as)
		self.script = script
		self.file_name = file_name
		self.pre_command = pre_command
		self.post_command = post_command

	def get_json(self):
		job_json = BaseJob.get_json(self)
		job_json['Type'] = 'Job:EmbeddedScript'
		if self.script != None:
			job_json['Script'] = self.script
		if self.file_name != None:
			job_json['FileName'] = self.file_name
		if self.pre_command != None:
			job_json['PreCommand'] = self.pre_command
		if self.post_command != None:
			job_json['PostCommand'] = self.post_command
		return job_json
