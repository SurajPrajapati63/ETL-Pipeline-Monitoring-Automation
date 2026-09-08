
from alerts.teams_alert import TeamsAlert


class AlertFactory:

    @staticmethod
    def create(alert_type):


        if alert_type == "teams":

            return TeamsAlert()

        raise Exception("Invalid Alert Type")