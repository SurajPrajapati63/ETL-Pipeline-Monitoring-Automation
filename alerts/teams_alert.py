import requests

from alerts.alert_service import AlertService
from config.config import Config


class TeamsAlert(AlertService):

    def send(self, subject, message):

        payload = {

            "title": subject,

            "text": message

        }

        response = requests.post(

            Config.TEAMS_WEBHOOK,

            json=payload

        )

        return response.status_code == 200