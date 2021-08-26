import unittest,json
from ctm-python-client.core import bmc_control_m as ctm-python-client
from ctm-python-client.jobs.hadoop.hdfs_commands import HDFSCommandsJob

class TestHDFSCommandsJob(unittest.TestCase):
	def test_HDFSCommandsJob(self):
		flow = ctm-python-client.CmJobFlow(application='',sub_application='')
		folder = flow.create_folder('test_folder')
		j = HDFSCommandsJob(folder=folder,job_name='test_job',
				connection_profile='connection_profile',
				commands='commands',
				host=None, run_as=None, description=None)
		jobs_params = {'Type', 'Commands', 'ConnectionProfile'}
		jobs_json = j.get_json()
		test_params = set(jobs_json.keys())
		print(test_params)
		self.assertEqual(jobs_params,test_params)
