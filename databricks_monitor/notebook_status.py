from databricks_monitor.databricks_api import DatabricksAPI


class NotebookStatus:

    def __init__(self):

        self.api = DatabricksAPI()

    def latest_run(self, job_id):

        data = self.api.get_runs(job_id)

        if not data["runs"]:

            return None

        run = data["runs"][0]

        return {

            "run_id": run["run_id"],

            "job_id": run["job_id"],

            "run_name": run["run_name"],

            "state": run["state"],

            "start_time": run.get("start_time"),

            "end_time": run.get("end_time"),

            "setup_duration": run.get("setup_duration"),

            "execution_duration": run.get("execution_duration"),

            "cleanup_duration": run.get("cleanup_duration"),

            "cluster_instance": run.get("cluster_instance")

        }