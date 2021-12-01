from abc import ABC, abstractmethod

from LogType import LogType


class AbstractLogger(ABC):
    @abstractmethod
    def log(self, message,logType:LogType):
        pass
