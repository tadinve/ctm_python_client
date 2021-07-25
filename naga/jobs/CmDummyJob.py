from naga.jobs.CmBaseJob import CmBaseJob


class CM_DummyJob(CM_BaseJob):
    def __init__(self,folder, jobName):
        CM_BaseJob.__init__(self,folder, jobName)
    def getJson(self):
        jobJson =  CM_BaseJob.getJson(self)
        jobJson["Type"] = "Job:Dummy" 
        return jobJson