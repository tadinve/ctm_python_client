from naga.core.base import BaseJob

class CreateJob(BaseJob):
	def __init__(self, folder, job_name, 
				path,
				search_interval,
				time_limit,
				start_time,
				stop_time,
				minimum_size,
				wild_card,
				minimal_age,
				maximal_age,
				host=None, run_as=None, description=None):

		BaseJob.__init__(self, folder, job_name, description=description, host=host, run_as=run_as)
		self.path = path
		self.search_interval = search_interval
		self.time_limit = time_limit
		self.start_time = start_time
		self.stop_time = stop_time
		self.minimum_size = minimum_size
		self.wild_card = wild_card
		self.minimal_age = minimal_age
		self.maximal_age = maximal_age

	def get_json(self):
		job_json = BaseJob.get_json(self)
		job_json['Type'] = 'Job:FileWatcher:Create'
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
		if self.minimum_size != None:
			job_json['MinimumSize'] = self.minimum_size
		if self.wild_card != None:
			job_json['WildCard'] = self.wild_card
		if self.minimal_age != None:
			job_json['MinimalAge'] = self.minimal_age
		if self.maximal_age != None:
			job_json['MaximalAge'] = self.maximal_age
		return job_json
