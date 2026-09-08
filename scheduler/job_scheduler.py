import schedule
import time

from blob_monitor.blob_listener import BlobListener

from monitoring.monitoring_engine import MonitoringEngine

from reports.report_generator import ReportGenerator

blob = BlobListener()

engine = MonitoringEngine()

report = ReportGenerator()

schedule.every(30).seconds.do(blob.monitor)

schedule.every(1).minutes.do(engine.process)

schedule.every(5).minutes.do(report.generate)

print("Job Scheduler Started...")

while True:

    schedule.run_pending()

    time.sleep(2)