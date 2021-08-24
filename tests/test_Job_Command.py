import unittest,json
from naga.core import bmc_control_m as naga
from naga.jobs.command import CommandJob

class TestCommandJob(unittest.TestCase):
	def test_CommandJob(self):
		flow = naga.CmJobFlow(application='',sub_application='')
		folder = flow.create_folder('test_folder')
		j = CommandJob(folder=folder,job_name='test_job',
				command='command',
				post_command='post_command',
				pre_command='pre_command',
				host=None, run_as=None, description=None)
		jobs_params = {'PreCommand', 'Type', 'Command', 'PostCommand'}
		jobs_json = j.get_json()
		test_params = set(jobs_json.keys())
		print(test_params)
		self.assertEqual(jobs_params,test_params)
