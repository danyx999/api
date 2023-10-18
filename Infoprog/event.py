from datetime import datetime
from global_variables import GlobalVariables


class Event:
    StartTime: str
    EndTime: str
    Date: str
    Text: str

    def __init__(self, start: str, end: str, date: str, text: str) -> None:
        startTime = datetime.strptime(start, GlobalVariables.TimeFormat)
        endTime = datetime.strptime(end, GlobalVariables.TimeFormat)
        eventDate = datetime.strptime(date, GlobalVariables.DateFormat)
        self.StartTime = startTime.strftime(GlobalVariables.TimeFormat)
        self.EndTime = endTime.strftime(GlobalVariables.TimeFormat)
        self.Date = eventDate.strftime(GlobalVariables.DateFormat)
        self.Text = text

    def CreateEventStr(self) -> str:
        return f"{GlobalVariables.Separator}".join(
            [self.Date, self.StartTime, self.EndTime, self.Text]
        )
