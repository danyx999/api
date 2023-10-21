from datetime import datetime
from global_variables import GlobalVariables


class EventChecker:
    def CheckTextLength(text: str) -> bool:
        if len(text) > GlobalVariables.MaxTextLength:
            return False
        else:
            return True

    def CheckDate(date: str) -> bool:
        try:
            datetime.strptime(date, GlobalVariables.DateFormat)
            return True
        except:
            return False

    def CheckTime(time: str) -> bool:
        try:
            datetime.strptime(time, GlobalVariables.TimeFormat)
            return True
        except:
            return False

    def CompareTimes(start: str, end: str) -> bool:
        startTime = datetime.strptime(start, GlobalVariables.TimeFormat)
        endTime = datetime.strptime(end, GlobalVariables.TimeFormat)

        if startTime < endTime:
            return True
        else:
            return False
