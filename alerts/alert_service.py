from abc import ABC, abstractmethod


class AlertService(ABC):

    @abstractmethod
    def send(self, subject, message):
        pass