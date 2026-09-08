from datetime import datetime

from monitoring.duration_calculator import DurationCalculator

from monitoring.status_tracker import StatusTracker

from database.repository import MonitoringRepository

from databricks_monitor.job_monitor import JobMonitor

from databricks_monitor.notebook_status import NotebookStatus

from databricks_monitor.cluster_monitor import ClusterMonitor
from alerts.alert_factory import AlertFactory

class MonitoringEngine:

    def __init__(self):
        self.repo = MonitoringRepository()
        self.job = JobMonitor()
        self.notebook = NotebookStatus()
        self.cluster = ClusterMonitor()

    def process(self):

        waiting = self.repo.fetch_waiting_files()

        job_id = self.job.get_job_id()

        if job_id is None:
            print("Job not found")
            return

        latest = self.notebook.latest_run(job_id)

        if latest is None:
            return

        start = DurationCalculator.ms_to_datetime(latest["start_time"])
        end = DurationCalculator.ms_to_datetime(latest["end_time"])

        formatted_start = start.strftime("%b %d, %Y, %I:%M %p") if start else None
        formatted_end = end.strftime("%b %d, %Y, %I:%M %p") if end else None

        cluster = self.cluster.cluster_details(latest["run_id"])
        status = StatusTracker.get_status(latest)

        for row in waiting:

            record_id = row[0]
            file_name = row[2]

            arrival = datetime.fromisoformat(row[1]) if isinstance(row[1], str) else row[1]

            queue = DurationCalculator.calculate_duration(arrival, start) if start and arrival and start > arrival else "0m 00s"

            notebook_duration = DurationCalculator.calculate_duration(start, end)
            total_duration = DurationCalculator.calculate_duration(arrival, end)

            self.repo.update_pipeline(
                record_id,
                formatted_start,
                queue,
                formatted_end,
                notebook_duration,
                total_duration,
                status,
                cluster.get("cluster_id")
            )

            # ✅ Send alert per file
            if status is not None:
                alert = AlertFactory.create("teams")

                subject = f"Pipeline {status}"

                message = f"""
File Name : {file_name}

Job ID : {latest['job_id']}
Run ID : {latest['run_id']}

Status : {status}

Queue Time : {queue}
Notebook Runtime : {notebook_duration}
Total Duration : {total_duration}
"""

                alert.send(subject, message)