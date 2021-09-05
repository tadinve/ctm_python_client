import os
import unittest
import json
import requests_mock

from ctm_python_client.core import bmc_control_m as ctm_python_client
from ctm_python_client.jobs.dummy import DummyJob


class TestCmJobFlow(unittest.TestCase):
    @staticmethod
    def get_default_job_flow():
        job = ctm_python_client.CmJobFlow(application="application",
                             sub_application="sub_application",
                             order_method="order_method",
                             description="description")
        return job

    @staticmethod
    def get_default_json() -> dict:
        expected_json = {"Defaults":
                             {"Application": "application",
                              "SubApplication": "sub_application",
                              "Description": "description",
                              "OrderMethod": "order_method"
                              },
                         }
        return expected_json

    def test_constructor(self):
        job_flow = self.get_default_job_flow()

        self.assertEqual(job_flow.application, "application")
        self.assertEqual(job_flow.sub_application, "sub_application")
        self.assertEqual(job_flow.folders, [])
        self.assertEqual(job_flow.jobs, [])
        self.assertEqual(job_flow.run_as_set, False)
        self.assertEqual(job_flow.schedule_set, False)
        self.assertEqual(job_flow.failure_notification, False)
        self.assertEqual(job_flow.flowcount, 0)
        self.assertEqual(job_flow.variables, [])

        expected_json = self.get_default_json()
        self.assertEqual(json.dumps(expected_json, sort_keys=True),
                         json.dumps(job_flow.json, sort_keys=True))


    def test_set_run_as(self):
        job_flow = self.get_default_job_flow()
        job_flow.set_run_as(username="username",
                            host="host",
                            ctm_server="ctm_server",
                            site_standard="site_standard")
        self.assertEqual(job_flow.username, "username")
        self.assertEqual(job_flow.host, "host")

        expected_json = self.get_default_json()
        expected_json["Defaults"].update({"RunAs": "username",
                                          "Host": "host",
                                          "ControlmServer": "ctm_server",
                                          "SiteStandard": "site_standard"})
        self.assertEqual(json.dumps(expected_json, sort_keys=True),
                         json.dumps(job_flow.json, sort_keys=True))

    def test_set_schedule(self):
        job_flow = self.get_default_job_flow()
        job_flow.set_schedule(months="months",
                              month_days="month_days",
                              week_days="week_days",
                              from_time="from_time",
                              to_time="to_time")

        self.assertEqual(job_flow.schedule_set, True)
        expected_schedule = {"Months": "months",
                             "MonthDays": "month_days",
                             "WeekDays": "week_days",
                             "FromTime": "from_time",
                             "ToTime": "to_time"}
        self.assertEqual(json.dumps(expected_schedule, sort_keys=True),
                         json.dumps(job_flow.json["Defaults"]["When"], sort_keys=True))

    def test_set_on_failure_notification(self):
        job_flow = self.get_default_job_flow()
        job_flow.set_on_failure_notification(mail_to="mail_to",
                                             mail_subject="mail_subject")

        self.assertEqual(job_flow.failure_notification, True)
        self.assertEqual(job_flow.mail_to, "mail_to")
        self.assertEqual(job_flow.mail_subject, "mail_subject")

    def test_str(self):
        job_flow = self.get_default_job_flow()
        expected_str = """{
                            "Defaults": {
                                "Application": "application",
                                "SubApplication": "sub_application",
                                "Description": "description",
                                "OrderMethod": "order_method"
                                }
                            }"""
        self.assertEqual(str(job_flow), str(job_flow))

    def test_create_folder(self):
        job_flow = self.get_default_job_flow()
        job_flow.create_folder(name="name", server="server")

        self.assertEqual(job_flow.folders, [["name", "server"]])
        self.assertEqual(job_flow.json["name"], {"Type": "Folder"})

        job_flow.create_folder(name="name2", server="server2")
        self.assertEqual(job_flow.folders, [["name", "server"],
                                            ["name2", "server2"]])
        self.assertEqual(job_flow.json["name2"], {"Type": "Folder"})
        # Make sure the first folder is not overwritten
        self.assertEqual(job_flow.json["name"], {"Type": "Folder"})

    def test_add_variables(self):
        job_flow = self.get_default_job_flow()
        job_flow.create_folder(name="folder", server="server")

        job_flow.add_variables(folder="folder",
                               list_of_variables=["var1", "var2"])
        self.assertEqual(job_flow.variables, ["var1", "var2"])

        job_flow.add_variables(folder="folder",
                               list_of_variables=["var3", "var4"])
        self.assertEqual(job_flow.variables, ["var1", "var2", "var3", "var4"])

        expected_json = self.get_default_json()
        expected_json.update({"folder": {"Type": "Folder",
                                         "Variables": ["var1", "var2", "var3", "var4"]}})

        self.assertEqual(expected_json, job_flow.json)

    def test_add_job(self):
        job_flow = self.get_default_job_flow()

        job = DummyJob(folder="folder", job_name="job_name")

        # Will throw error, since there is no folder
        with self.assertRaises(KeyError):
            job_flow.add_job(folder="folder", job=job)

        # Add Folder and then, add job
        job_flow.create_folder(name="folder", server="server")

        job_flow.add_job(folder="folder", job=job)

        self.assertEqual(job_flow.json["folder"]["job_name"], job.get_json())
        self.assertEqual(job_flow.jobs[0][0], "job_name")

    def test_chain_jobs(self):
        job_flow = self.get_default_job_flow()
        job1 = DummyJob(folder="folder", job_name="job1")
        job2 = DummyJob(folder="folder", job_name="job2")

        job_flow.create_folder(name="folder", server="server")

        job_id1 = job_flow.add_job("folder", job1)
        job_id2 = job_flow.add_job("folder", job2)

        job_flow.chain_jobs("folder", [job_id1, job_id2])

        self.assertEqual(job_flow.flowcount, 1)

        expected_json = {"Defaults": {"Application": "application",
                                      "Description": "description",
                                      "OrderMethod": "order_method",
                                      "SubApplication": "sub_application"},
                         "folder": {"Flow1": {"Sequence": ["job1", "job2"],
                                              "Type": "Flow"},
                                    "Type": "Folder",
                                    "job1": {"Type": None},
                                    "job2": {"Type": None}}}
        #self.assertEqual(json.dumps(expected_json, sort_keys=True),
        #                 json.dumps(job_flow.json, sort_keys=True))

    def test_display(self):
        job_flow = self.get_default_job_flow()
        job_flow.create_folder("folder", "server")
        job_flow.set_run_as(username="username",
                            host="host",
                            ctm_server="ctm_server",
                            site_standard="site_standard")
        job_flow.set_on_failure_notification(mail_to="mail_to",
                                             mail_subject="mail_subject")

        g = job_flow.display()
        self.assertIsNotNone(g)

