from blob_monitor.blob_listener import BlobListener

from monitoring.monitoring_engine import MonitoringEngine

from reports.report_generator import ReportGenerator

from alerts.alert_factory import AlertFactory

from config.loggers import get_logger

logger = get_logger()


class MonitorRunner:

    def __init__(self):

        self.blob = BlobListener()

        self.engine = MonitoringEngine()

        self.report = ReportGenerator()

        self.alert = AlertFactory.create("teams")

    def run(self):

        try:

            logger.info("Checking Blob Storage...")

            self.blob.monitor()

            logger.info("Blob Monitoring Completed")

            logger.info("Checking Databricks...")

            self.engine.process()

            logger.info("Monitoring Engine Completed")

            logger.info("Generating Excel...")

            self.report.generate()

            logger.info("Excel Generated")

            self.alert.send(

                "Pipeline Monitoring",

                "Pipeline Monitoring Completed Successfully"

            )

        except Exception as ex:

            logger.exception(ex)

            self.alert.send(

                "Pipeline Monitoring Failed",

                str(ex)

            )