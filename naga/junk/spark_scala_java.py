from naga.jobs.base import BaseJob


class SparkScalaJavaJob(BaseJob):
    def __init__(
        self,
        folder,
        job_name,
        connection_profile,
        program_jar,
        main_class,
        arguments,
        pre_commands,
        output,
        host=None,
        run_as=None,
        description=None,
    ):
        BaseJob.__init__(self, folder, job_name, description, host, run_as)
        self.connection_profile = connection_profile
        self.program_jar = program_jar
        self.main_class = main_class
        self.arguments = arguments
        self.output = output
        self.pre_commands = pre_commands

    def get_json(self):
        job_json = BaseJob.get_json(self)
        job_json["Type"] = "Job:Hadoop:Spark:ScalaJava"
        job_json["ConnectionProfile"] = self.connection_profile
        job_json["ProgramJar"] = self.program_jar
        job_json["MainClass"] = self.main_class
        job_json["Arguments"] = self.arguments
        job_json["PreCommands"] = self.pre_commands
        job_json["Output"] = self.output
        return job_json
