from ConsoleLogger import ConsoleLogger
from LogType import LogType
from LoggerCollection import LoggerCollection
from TxtLogger import TxtLogger

if __name__ == '__main__':
    logger = ConsoleLogger()
    txtLogger = TxtLogger(r"C:\Temp\logTest.txt")
    loggerCollection = LoggerCollection([txtLogger,logger])
    loggerCollection.log("dit es een message", LogType.ERROR)


