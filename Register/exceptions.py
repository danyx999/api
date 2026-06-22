class AllRegistersClosedException(Exception):
    def __init__(self) -> None:
        super().__init__()
        self.Message = f"All registers are closed"