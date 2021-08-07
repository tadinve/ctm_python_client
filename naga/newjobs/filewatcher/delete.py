from naga.jobs.base import BaseJob

class DeleteJob(BaseJob):
	def __init__(self, folder, job_name, 
				path,
				search_interval,
				time_limit,
				start_time,
				stop_time,
				type = None,
				run_as = None,
				host = None,
		BaseJob.__init__(self, folder, job_name, description=description, host=host, run_as=run_as)
		self.path = path
		self.search_interval = search_interval
		self.time_limit = time_limit
		self.start_time = start_time
		self.stop_time = stop_time
		self.type = type
		self.run_as = run_as
		self.host = host

	def get_json(self):
		job_json = BaseJob.get_json(self)
		job_json['Type'] = 'Job:FileWatcher:Delete'
		if self.path != None:
			job_json['Path'] = self.path
		if self.search_interval != None:
			job_json['SearchInterval'] = self.search_interval
		if self.time_limit != None:
			job_json['TimeLimit'] = self.time_limit
		if self.start_time != None:
			job_json['StartTime'] = self.start_time
		if self.stop_time != None:
			job_json['StopTime'] = self.stop_time
		if self.type != None:
			job_json['Type'] = self.type
		if self.run_as != None:
			job_json['RunAs'] = self.run_as
		if self.host != None:
			job_json['Host'] = self.host
		return job_json
