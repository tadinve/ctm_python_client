import unittest,json
from ctm-python-client.core import bmc_control_m as ctm-python-client
from ctm-python-client.jobs.sap.r3.copy import COPYJob

class TestCOPYJob(unittest.TestCase):
	def test_COPYJob(self):
		flow = ctm-python-client.CmJobFlow(application='',sub_application='')
		folder = flow.create_folder('test_folder')
		j = COPYJob(folder=folder,job_name='test_job',
				connection_profile='connection_profile',
				sap_job_name='sap_job_name',
				exec='exec',
				target='target',
				job_count='job_count',
				job_count_specific_name='job_count_specific_name',
				new_job_name='new_job_name',
				start_condition='start_condition',
				after_event='after_event',
				after_event_parameters='after_event_parameters',
				rerun_from_point_of_failure='rerun_from_point_of_failure',
				copy_from_step='copy_from_step',
				post_job_action='post_job_action',
				detect_spawned_job='detect_spawned_job',
				host=None, run_as=None, description=None)
		jobs_params = {'Exec', 'JobCountSpecificName', 'CopyFromStep', 'Target', 'Type', 'ConnectionProfile', 'JobCount', 'PostJobAction', 'NewJobName', 'RerunFromPointOfFailure', 'DetectSpawnedJob', 'SapJobName', 'StartCondition', 'AfterEvent', 'AfterEventParameters'}
		jobs_json = j.get_json()
		test_params = set(jobs_json.keys())
		print(test_params)
		self.assertEqual(jobs_params,test_params)
