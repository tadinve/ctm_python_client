from naga.jobs.base import BaseJob

class FileTransferJob(BaseJob):
	def __init__(self, folder, job_name, 
				connection_profile_src,
				connection_profile_dest,
				number_of_retries,
				s3_bucket_name,
				file_transfers,
				type = None,
				run_as = None,
				host = None,
		BaseJob.__init__(self, folder, job_name, description=description, host=host, run_as=run_as)
		self.connection_profile_src = connection_profile_src
		self.connection_profile_dest = connection_profile_dest
		self.number_of_retries = number_of_retries
		self.s3_bucket_name = s3_bucket_name
		self.file_transfers = file_transfers
		self.type = type
		self.run_as = run_as
		self.host = host

	def get_json(self):
		job_json = BaseJob.get_json(self)
		job_json['Type'] = 'Job:FileTransfer'
		if self.connection_profile_src != None:
			job_json['ConnectionProfileSrc'] = self.connection_profile_src
		if self.connection_profile_dest != None:
			job_json['ConnectionProfileDest'] = self.connection_profile_dest
		if self.number_of_retries != None:
			job_json['NumberOfRetries'] = self.number_of_retries
		if self.s3_bucket_name != None:
			job_json['S3BucketName'] = self.s3_bucket_name
		if self.file_transfers != None:
			job_json['FileTransfers'] = self.file_transfers
		if self.type != None:
			job_json['Type'] = self.type
		if self.run_as != None:
			job_json['RunAs'] = self.run_as
		if self.host != None:
			job_json['Host'] = self.host
		return job_json
