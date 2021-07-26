"""
Copyright (c) 2012-2021 BMC, Inc. and others

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# This class is based on https://docs.bmc.com/docs/automation-api/918/code-reference-783053198.html


"""
import os
import json
import requests
from graphviz import Digraph


JOBS_FILE = "jobs.json"


class CmJobFlow:

    # Constructor and setting some default values
    def __init__(self, application, sub_application, description=None, order_method=None):
        self.application = application
        self.sub_application = sub_application
        self.folders = []
        self.jobs = []
        self.run_as_set = False
        self.schedule_set = False
        self.failure_notification = False

        self.graph = Digraph("G", filename=application + ".gv")
        # self.g.attr(rankdir='LR', size='8,5',  shape='rectangle')
        self.graph.attr(shape="ellipse")

        self.flowcount = 0
        self.variables = []

        self.json = {"Defaults": {"Application": application, "SubApplication": sub_application}}
        if description is not None:
            self.json["Defaults"]["Description"] = description
        if order_method is not None:
            self.json["Defaults"]["OrderMethod"] = order_method

        # Attributes used in methods
        self.uri = None
        self.token = None
        self.https = None
        self.username = None
        self.password = None
        self.host = None
        self.schedule = None
        self.mail_to = None
        self.mail_subject = None

    def ctm_login_saas(self, ctm_uri, ctm_token, https=True):
        self.uri = ctm_uri
        self.token = ctm_token
        self.https = https

    def authenticate(self, credentials_file, https=True):
        self.https = https
        with open(credentials_file) as json_file:
            credentials = json.load(json_file)
            self.username = credentials["user"]
            self.password = credentials["password"]
            self.uri = credentials["uri"]

        # login
        r_login = requests.post(
            self.uri + "/automation-api/session/login",
            json={"username": self.username, "password": self.password},
            verify=self.https,
        )

        if r_login.status_code != requests.codes.ok:
            print("Failure Logining into ", self.uri)
            print(r_login.content)
            return r_login.status_code

        print("Successfully logged into ", self.uri)
        self.token = r_login.json()["token"]
        print("Token =", self.token)
        return r_login.status_code

    def ctm_login(self, ctm_uri, ctm_user, ctm_pwd, https=True):
        self.uri = ctm_uri
        self.username = ctm_user
        self.password = ctm_pwd
        self.https = https

        # login
        r_login = requests.post(
            self.uri + "/automation-api/session/login",
            json={"username": self.username, "password": self.password},
            verify=self.https,
        )

        if r_login.status_code != requests.codes.ok:
            print("Failure Logining into ", self.uri)
            print(r_login.content)
            return r_login.status_code

        print("Successfully logged into ", self.uri)
        self.token = r_login.json()["token"]
        print("Token =", self.token)
        return r_login.status_code
        # this is a private functions defined to create nodes in the graph

    def _create_node(self, name, shape="box"):
        self.jobs.append(name)
        node_id = str(len(self.jobs) - 1)
        self.graph.node(node_id, label=name, shape=shape)
        return node_id

        # sets up the default user to run the jobs (can be overridden at the job level)

    def set_run_as(self, username, host, ctm_server=None, site_standard=None):
        self.run_as_set = True
        self.username = username
        self.host = host
        self.json["Defaults"]["RunAs"] = username
        self.json["Defaults"]["Host"] = host
        if ctm_server is not None:
            self.json["Defaults"]["ControlmServer"] = ctm_server
        if site_standard is not None:
            self.json["Defaults"]["SiteStandard"] = site_standard

    # sets up the default user to run the jobs (can be overridden at the job level)
    def set_schedule(self, months=None, month_days=None, week_days=None, from_time=None, to_time=None):
        self.schedule_set = True
        self.json["Defaults"]["When"] = {}
        if months is not None:
            self.json["Defaults"]["When"]["Months"] = months
        if month_days is not None:
            self.json["Defaults"]["When"]["MonthDays"] = month_days
        if week_days is not None:
            self.json["Defaults"]["When"]["WeekDays"] = week_days
        if from_time is not None:
            self.json["Defaults"]["When"]["FromTime"] = from_time
        if to_time is not None:
            self.json["Defaults"]["When"]["ToTime"] = to_time

    # Whom to email on any job failure
    def set_on_failure_notification(self, mail_to, mail_subject):
        self.failure_notification = True
        self.mail_to = mail_to
        self.mail_subject = mail_subject

    def __str__(self):
        return json.dumps(self.json, indent=4)

    def submit(self):
        with open(JOBS_FILE, "w") as outfile:
            json.dump(self.json, outfile, indent=4)

        with open(JOBS_FILE, "rb") as fo_jobs:
            uploaded_files = [("definitionsFile", (JOBS_FILE, fo_jobs, "application/json"))]
            r_submit = requests.post(
                self.uri + "/automation-api/deploy",
                files=uploaded_files,
                headers={"Authorization": "Bearer " + self.token},
                verify=self.https,
            )
            print(r_submit.content)

        # Remove temporary file
        os.remove(JOBS_FILE)

        print(r_submit.status_code)
        j = json.loads(r_submit.content)
        if "errors" in j:
            for msg in j["errors"]:
                print(msg)
        if r_submit.status_code != requests.codes.ok:
            print("Failure Submitting")
            return r_submit.status_code

        print("Successfully submitted to Control-M")
        print("Login to {0}/ControlM/ and use your workflow".format(self.uri))
        return r_submit.status_code

    def run(self):
        with open(JOBS_FILE, "w") as outfile:
            json.dump(self.json, outfile, indent=4)

        with open(JOBS_FILE, "rb") as fo_jobs:
            uploaded_files = [("definitionsFile", (JOBS_FILE, fo_jobs, "application/json"))]
            r_submit = requests.post(
                self.uri + "/automation-api/run",
                files=uploaded_files,
                headers={"Authorization": "Bearer " + self.token},
                verify=self.https,
            )
            print(r_submit.content)

        # Remove temporary file
        os.remove(JOBS_FILE)

        print(r_submit.status_code)
        j = json.loads(r_submit.content)
        if "errors" in j:
            for msg in j["errors"]:
                print(msg)
        if r_submit.status_code != requests.codes.ok:
            print("Failure Submitting")
            return r_submit.status_code

        print("Successfully submitted to Control-M")
        print("Login to {0}/ControlM/ and use your workflow".format(self.uri))
        return r_submit.status_code



    def submit_saas(self):
        with open(JOBS_FILE, "w") as outfile:
            json.dump(self.json, outfile, indent=4)

        with open(JOBS_FILE, "rb") as fo_jobs:
            uploaded_files = [("definitionsFile", (JOBS_FILE, fo_jobs, "application/json"))]
            r_submit = requests.post(
                self.uri + "/automation-api/deploy",
                files=uploaded_files,
                headers={"x-api-key": self.token},
                verify=self.https,
            )
        # Remove temporary file
        os.remove(JOBS_FILE)

        print(r_submit.content)
        print(r_submit.status_code)
        j = json.loads(r_submit.content)
        if "errors" in j:
            for msg in j["errors"]:
                print(msg)
        if r_submit.status_code != requests.codes.ok:
            print("Failure Submitting")
            return r_submit.status_code

        print("Successfully submitted to Control-M")
        print("Login to {0}/ControlM/ and use your workflow".format(self.uri))
        return r_submit.status_code

    # This function displays the Jobflow
    def display(self):
        print("=========== Jobflow Details ===================")
        print("Application: ", self.application)
        print("Sub Application: ", self.sub_application)

        if self.run_as_set:
            print("\nRun as Username: {0} on Host: {1}".format(self.username, self.host))

        for folder in self.folders:
            print("\nFolder Name {0} with Server {1}\n\n\n".format(folder[0], folder[1]))

        if self.failure_notification:
            print("\n On Failure notify {0} with Subject {1}".format(self.mail_to, self.mail_subject))

        return self.graph

    def display_json(self):
        str = json.dumps(self.json, indent=4)
        print(str)

    def get_json_for_folder(self, folder_name):

        r_submit = requests.get(
            self.uri + "/automation-api/deploy/jobs?ctm=*&folder=" + folder_name,
            headers={"Authorization": "Bearer " + self.token},
            verify=self.https,
        )

        print(r_submit.status_code)
        j = json.loads(r_submit.content)
        if "errors" in j:
            for msg in j["errors"]:
                print(msg)

        if r_submit.status_code != requests.codes.ok:
            print("Failure Submitting")
            return r_submit.status_code

        print(r_submit.content)
        print("Successfully extracted JSON format for folder {} to Control-M".format(folder_name))

        return j

    # Jobs can be grouped together as folders, this creates the folder
    def create_folder(self, name, server=None):
        self.folders.append([name, server])
        self.json[name] = {"Type": "Folder"}
        return name

    # sets up the default user to run the jobs (can be overridden at the job level)
    def add_variables(self, folder, list_of_variables):
        self.variables += list_of_variables
        self.json[folder]["Variables"] = self.variables

    def add_job(self, folder, job):
        job_name = job.get_job_name()
        self.json[folder][job_name] = job.get_json()
        return self._create_node(job_name, shape="Msquare")

    # this function sets up dependencies of jobs, and used to define job execution sequence.
    def chain_jobs(self, folder, links):
        print(self.jobs)
        print(links)
        self.flowcount += 1

        from_job = links[0]
        seq = [
            self.jobs[int(links[0])],
        ]
        for j in links[1:]:
            self.graph.edge(from_job, j)
            from_job = j
            seq.append(self.jobs[int(j)])
        self.json[folder]["Flow" + str(self.flowcount)] = {"Type": "Flow", "Sequence": seq}
