from ConsoleLogger import ConsoleLogger
from LogType import LogType

if __name__ == '__main__':
    logger = ConsoleLogger()
    logger.log("dit es een message", LogType.ERROR)
