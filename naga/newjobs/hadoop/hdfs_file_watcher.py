from naga.jobs.base import BaseJob

class HDFSFileWatcherJob(BaseJob):
	def __init__(self, folder, job_name, 
				connection_profile,
				hdfs_file_path,
				min_deteced_size,
				max_wait_time,
				type = None,
				run_as = None,
				host = None,
		BaseJob.__init__(self, folder, job_name, description=description, host=host, run_as=run_as)
		self.connection_profile = connection_profile
		self.hdfs_file_path = hdfs_file_path
		self.min_deteced_size = min_deteced_size
		self.max_wait_time = max_wait_time
		self.type = type
		self.run_as = run_as
		self.host = host

	def get_json(self):
		job_json = BaseJob.get_json(self)
		job_json['Type'] = 'Job:Hadoop:HDFSFileWatcher'
		if self.connection_profile != None:
			job_json['ConnectionProfile'] = self.connection_profile
		if self.hdfs_file_path != None:
			job_json['HdfsFilePath'] = self.hdfs_file_path
		if self.min_deteced_size != None:
			job_json['MinDetecedSize'] = self.min_deteced_size
		if self.max_wait_time != None:
			job_json['MaxWaitTime'] = self.max_wait_time
		if self.type != None:
			job_json['Type'] = self.type
		if self.run_as != None:
			job_json['RunAs'] = self.run_as
		if self.host != None:
			job_json['Host'] = self.host
		return job_json
