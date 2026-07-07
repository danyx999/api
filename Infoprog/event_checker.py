from datetime import datetime
from global_variables import GlobalVariables


class EventChecker:
    @staticmethod
    def CheckTextLength(text: str) -> bool:
        if len(text) > GlobalVariables.MaxTextLength:
            return False
        else:
            return True

    @staticmethod
    def CheckDate(date: str) -> bool:
        try:
            datetime.strptime(date, GlobalVariables.DateFormat)
            return True
        except:
            return False

    @staticmethod
    def CheckTime(time: str) -> bool:
        try:
            datetime.strptime(time, GlobalVariables.TimeFormat)
            return True
        except:
            return False

    @staticmethod
    def CompareTimes(start: str, end: str) -> bool:
        startTime = datetime.strptime(start, GlobalVariables.TimeFormat)
        endTime = datetime.strptime(end, GlobalVariables.TimeFormat)

        if startTime < endTime:
            return True
        else:
            return False
