from naga.jobs.base import BaseJob


class FileTransferJob(BaseJob):
    def __init__(self, folder, job_name, connection_src, connection_dest, host=None, run_as=None, description=None):
        BaseJob.__init__(self, folder, job_name, description, host, run_as)
        self.connection_src = connection_src
        self.connection_dest = connection_dest
        self.transfers = []

    def add_file_transfer(self, src, dest, option, transfer_type=None):
        transfer = {"Src": src,
                    "Dest": dest,
                    "TransferOption": option}
        if transfer_type is not None:
            transfer["TransferType"] = transfer_type
        self.transfers.append(transfer)

    def get_json(self):
        job_json = BaseJob.get_json(self)
        job_json["Type"] = "Job:FileTransfer"
        job_json["ConnectionProfileSrc"] = self.connection_src
        job_json["ConnectionProfileDest"] = self.connection_dest
        job_json["FileTransfers"] = self.transfers
        return job_json