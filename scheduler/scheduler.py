import schedule
import time

from scheduler.monitor_runner import MonitorRunner

runner = MonitorRunner()


def execute():

    print("=" * 60)
    print("Pipeline Monitoring Started")
    print("=" * 60)

    runner.run()

    print("=" * 60)
    print("Monitoring Completed")
    print("=" * 60)


schedule.every(1).minutes.do(execute)

print("Scheduler Started...")

execute()

while True:

    schedule.run_pending()

    time.sleep(5)