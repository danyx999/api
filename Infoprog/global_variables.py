from os import path


class GlobalVariables:
    MaxTextLength: int = 250
    DateFormat: str = "%d.%m.%Y"
    TimeFormat: str = "%H:%M"
    Separator: str = ";"
    FilePath: str = f"{path.dirname(__file__)}\\events.txt"
    Exit: str = "0"
