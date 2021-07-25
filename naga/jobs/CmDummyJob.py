from naga.jobs.CmBaseJob import CmBaseJob


class CmDummyJob(CmBaseJob):
    def __init__(self,folder, jobName):
        CmBaseJob.__init__(self,folder, jobName)
    def getJson(self):
        jobJson =  CmBaseJob.getJson(self)
        jobJson["Type"] = "Job:Dummy" 
        return jobJson