from databricks_monitor.job_monitor import JobMonitor
from databricks_monitor.notebook_status import NotebookStatus
from databricks_monitor.cluster_monitor import ClusterMonitor


job = JobMonitor()

job_id = job.get_job_id()

print("Job ID:", job_id)

status = NotebookStatus()

run = status.latest_run(job_id)

print(run)

cluster = ClusterMonitor()

print(cluster.cluster_details(run["run_id"]))