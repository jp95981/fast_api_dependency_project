class SlurmClient:
    def __init__(self):
        self._session = None  # Dependency injection this session

    def submit_job(self, cmd):
        raise NotImplementedError

    def get_job_status(self, job_id):
        raise NotImplementedError

    def cancel_job(self, job_id):
        raise NotImplementedError

    def get_job_output(self, job_id):
        raise NotImplementedError

    def ping(self):
        print(f"{__file__} is Working!!!")
