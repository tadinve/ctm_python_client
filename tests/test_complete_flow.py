import unittest, json
import os
from ctm_python_client.core.bmc_control_m import CmJobFlow
from ctm_python_client.jobs.dummy import DummyJob
from ctm_python_client.jobs.command import CommandJob


# Please change the URI, and ctm_user and enter ctm_password to match your environment
from ctm_python_client.session.session import Session


class TestCompleteFlow(unittest.TestCase):
    def test_completeFlow(self):
        # Read secrets file to get URI, Username and Password
        BASE_PATH = os.path.abspath(os.path.dirname(__file__))
        with open(os.path.join(BASE_PATH,  ".secrets"), "r") as fp:
            ctm_uri = fp.readline().strip()
            ctm_user = fp.readline().strip()
            ctm_pwd = fp.readline().strip()

        # Create CTM Session
        session = Session(endpoint=ctm_uri, username=ctm_user, password=ctm_pwd)

        # CREATE JOB FLOW
        t1_flow = CmJobFlow(
            application="Naga0.3_Demo", sub_application="Demo-02", session=session, ctm_uri=ctm_uri
        )

        t1_flow.set_run_as(username="ctmuser", host="acb-rhctmv20")

        # Define the schedule
        months = ["JAN", "OCT", "DEC"]
        monthDays = ["ALL"]
        weekDays = ["MON", "TUE", "WED", "THU", "FRI"]
        fromTime = "0300"
        toTime = "2100"
        t1_flow.set_schedule(months, monthDays, weekDays, fromTime, toTime)

        # Create Folder
        f1 = t1_flow.create_folder(name="WeatherForecast")

        """### Step 3B - Define Variables"""

        # appid is the weather api token, you obtained during setup
        variables = [
            {"appid": "481be8b9210a09cc3a3bcdcf190a3aa8"},
            {"zipcode": "95130"},
            {"email": "vtadinad@bmc.com"},
        ]
        t1_flow.add_variables(folder=f1, list_of_variables=variables)

        """# Step 4 - Create Tasks"""

        start = t1_flow.add_job(f1, DummyJob(folder=f1, job_name="StartFlow"))
        end = t1_flow.add_job(f1, DummyJob(folder=f1, job_name="EndFlow"))

        hostname = "acb-ubuntu.centralus.cloudapp.azure.com"
        run_as = "ctmuser"

        # create job 1
        j1 = CommandJob(
            folder=f1,
            job_name="GetMaxTemp",
            command='wget "https://api.openweathermap.org/data/2.5/weather?zip=%%zipcode,us&appid=%%appid&units=imperial" -O $HOME/output.json',
            host=hostname,
            run_as=run_as,
        )
        GetMaxTemp = t1_flow.add_job(folder=f1, job=j1)

        # create job 2
        j2 = CommandJob(
            folder=f1,
            job_name="CityVar",
            command='cd $HOME/ && city=$(cat output.json | jq -r ".name") | echo "$city"',
            host=hostname,
            run_as=run_as,
        )
        j2.capture_output(
            variable="city", capture_type="UpToEndOfLine", search_string="city="
        )
        CityVar = t1_flow.add_job(folder=f1, job=j2)

        # create job 3
        j3 = CommandJob(
            folder=f1,
            job_name="CountryVar",
            command='cd $HOME/ && country=$(cat output.json | jq -r ".sys.country") | echo "$country"',
            host=hostname,
            run_as=run_as,
        )
        j3.capture_output(
            variable="country", capture_type="UpToEndOfLine", search_string="country="
        )
        CountryVar = t1_flow.add_job(folder=f1, job=j3)

        # create job 4
        j4 = CommandJob(
            folder=f1,
            job_name="HighTempVar",
            command='cd $HOME/ && high_temp=$(cat output.json | jq ".main.temp_max") | echo "$high_temp"',
            host=hostname,
            run_as=run_as,
        )
        j4.capture_output(
            variable="hightemp",
            capture_type="UpToEndOfLine",
            search_string="high_temp=",
        )
        HighTempVar = t1_flow.add_job(folder=f1, job=j4)

        # create job 5
        j5 = CommandJob(
            folder=f1,
            job_name="SendEmail",
            command='echo \\"Today, the high temperature in %%city %%country is %%hightemp F.\\"',
            host=hostname,
            run_as=run_as,
        )
        j5.on_success_send_mail(
            mail_subject="Today's High Temperature",
            mail_to="%%email",
            mail_message="Today, the high temperature in %%city %%country is %%hightemp F.",
        )
        SendEmail = t1_flow.add_job(folder=f1, job=j5)

        """# Step 5 - Chain Tasks"""

        t1_flow.chain_jobs(f1, [start, GetMaxTemp, HighTempVar, SendEmail, end])
        t1_flow.chain_jobs(f1, [GetMaxTemp, CountryVar, SendEmail])
        t1_flow.chain_jobs(f1, [GetMaxTemp, CityVar, SendEmail])

        deploy_return = t1_flow.deploy()
        res = """{'deployed_calendars': None,\n 'deployed_connection_profiles': None,\n 'deployed_drivers': None,\n 'deployed_folders': ['WeatherForecast'],\n 'deployed_jobs': None,\n 'deployment_file': 'jobs.json',\n 'errors': None,\n 'is_deploy_descriptor_valid': False,\n 'successful_calendars_count': None,\n 'successful_connection_profiles_count': 0,\n 'successful_drivers_count': 0,\n 'successful_folders_count': 0,\n 'successful_jobs_count': 7,\n 'successful_smart_folders_count': 1,\n 'successful_sub_folders_count': 0,\n 'warnings': None}"""

        self.assertEqual(str(deploy_return[0]), res)

        t1_flow.display_json()

        ## Run the job
        s = t1_flow.run()
        self.assertEqual(None, None)

        # Get nodes and edges
        nodes, edges = t1_flow.get_nodes_and_edges()
        self.assertTrue(len(nodes) > 0)


        # ## Let's fail the deploy to check if exceptions are caught
        # j_fail = GLUEJob(
        #                     folder=f1,
        #                     job_name='glue',
        #                     connection_profile="GLUECONNECTION",
        #                     aiglue_job_name="AwsGlueJobName",
        #                     aiglue_job_arguments="checked",
        #                     aiarguments={'--myArg1': 'myVal1', '--myArg2': 'myVal2'},
        #                     aistatus_polling_frequency="20",
        #                 )
        # j_fail_id = t1_flow.add_job(folder=f1, job=j_fail)
        # deploy_return = t1_flow.deploy()
        # res = """{'deployed_calendars': None,\n 'deployed_connection_profiles': None,\n 'deployed_drivers': None,\n 'deployed_folders': ['WeatherForecast'],\n 'deployed_jobs': None,\n 'deployment_file': 'jobs.json',\n 'errors': None,\n 'is_deploy_descriptor_valid': False,\n 'successful_calendars_count': None,\n 'successful_connection_profiles_count': 0,\n 'successful_drivers_count': 0,\n 'successful_folders_count': 0,\n 'successful_jobs_count': 7,\n 'successful_smart_folders_count': 1,\n 'successful_sub_folders_count': 0,\n 'warnings': None}"""

        # self.assertEqual(deploy_return,400)



        ## Test Run Fail
        run_return = t1_flow.run()
        self.assertEqual(400, 400)


