from AbstractLogger import AbstractLogger
from LogType import LogType


class NoneLogger(AbstractLogger):
    def log(self, message: str, logType: LogType):
        pass