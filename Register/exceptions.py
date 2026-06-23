class AllRegistersClosedException(Exception):
    def __init__(self) -> None:
        super().__init__()
        self.Message = f"All registers are closed"

class AllRegistersOpenException(Exception):
    def __init__(self) -> None:
        super().__init__()
        self.Message = f"All registers are open"

class RegisterAlreadyOpenException(Exception):
    def __init__(self) -> None:
        super().__init__()
        self.Message = f"This Register is already open"

class RegisterAlreadyClosedException(Exception):
    def __init__(self) -> None:
        super().__init__()
        self.Message = f"This register is already closed"