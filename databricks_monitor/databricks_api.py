import requests

from config.config import Config


class DatabricksAPI:

    def __init__(self):

        self.host = Config.DATABRICKS_HOST

        self.headers = {
            "Authorization": f"Bearer {Config.DATABRICKS_TOKEN}"
        }

    def get_jobs(self):

        url = f"{self.host}/api/2.1/jobs/list"

        response = requests.get(
            url,
            headers=self.headers
        )

        response.raise_for_status()

        return response.json()

    def get_runs(self, job_id):

        url = f"{self.host}/api/2.1/jobs/runs/list"

        params = {

            "job_id": job_id,

            "limit": 1

        }

        response = requests.get(

            url,

            headers=self.headers,

            params=params

        )

        response.raise_for_status()

        return response.json()

    def get_run(self, run_id):

        url = f"{self.host}/api/2.1/jobs/runs/get"

        params = {

            "run_id": run_id

        }

        response = requests.get(

            url,

            headers=self.headers,

            params=params

        )

        response.raise_for_status()

        return response.json()