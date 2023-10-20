from datetime import datetime
from global_variables import GlobalVariables


class Event:
    StartTime: datetime
    EndTime: datetime
    Date: datetime
    Text: str

    def __init__(self, start: str, end: str, date: str, text: str) -> None:
        self.StartTime = datetime.strptime(start, GlobalVariables.TimeFormat)
        self.EndTime = datetime.strptime(end, GlobalVariables.TimeFormat)
        self.Date = datetime.strptime(date, GlobalVariables.DateFormat)
        self.Text = text

    def CreateEventStr(self) -> str:
        return f"{GlobalVariables.Separator}".join(
            [
                self.StartTime.strftime(GlobalVariables.TimeFormat),
                self.EndTime.strftime(GlobalVariables.TimeFormat),
                self.Date.strftime(GlobalVariables.DateFormat),
                self.Text,
            ]
        )
