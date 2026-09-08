import schedule
import time

from blob_monitor.blob_listener import BlobListener

listener = BlobListener()

schedule.every(1).minutes.do(listener.monitor)

print("Blob Scheduler Started")

while True:

    schedule.run_pending()

    time.sleep(5)