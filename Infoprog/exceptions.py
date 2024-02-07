from global_variables import GlobalVariables


class TextIsLongerThanMaxTextLengthException(Exception):
    def __init__(self) -> None:
        super().__init__()
        self.Text = f"Your note is longer than {GlobalVariables.MaxTextLength}"


class StartTimeIsLaterThanEndTimeException(Exception):
    def __init__(self) -> None:
        super().__init__()
        self.Text = f"Start time is later than end time"


class IncorrectDateException(Exception):
    def __init__(self) -> None:
        super().__init__()
        self.Text = f"Incorrectly entered date"


class IncorrectTimeException(Exception):
    def __init__(self) -> None:
        super().__init__()
        self.Text = f"Incorrectly entered time"


class IncorrectOptionException(Exception):
    def __init__(self) -> None:
        super().__init__()
        self.Text = f"Incorrectly entered option"


class IncorrectModeException(Exception):
    def __init__(self) -> None:
        super().__init__()
        self.Text = f"Incorrectly entered mode"
