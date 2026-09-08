from databricks_monitor.databricks_api import DatabricksAPI


class ClusterMonitor:

    def __init__(self):

        self.api = DatabricksAPI()

    def cluster_details(self, run_id):

        run = self.api.get_run(run_id)

        cluster = run.get("cluster_instance", {})

        return {

            "cluster_id": cluster.get("cluster_id"),

            "spark_context_id": cluster.get("spark_context_id")

        }