from databricks_monitor.databricks_api import DatabricksAPI
from config.config import Config


class JobMonitor:

    def __init__(self):

        self.api = DatabricksAPI()

    def get_job_id(self):

        jobs = self.api.get_jobs()

        for job in jobs.get("jobs", []):

            if job["settings"]["name"] == Config.JOB_NAME:

                return job["job_id"]

        return None