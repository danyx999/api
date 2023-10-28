from global_variables import GlobalVariables


class TextIsLongerThanMaxTextLengthException(Exception):
    def __init__(self) -> None:
        super().__init__()
        self.Text = f"Your note is longer than {GlobalVariables.MaxTextLength}"


class StartTimeIsLaterThanEndTimeException(Exception):
    def __init__(self) -> None:
        super().__init__()
        self.Text = f"Start date is later than end date"


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
