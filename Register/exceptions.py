class AllRegistersClosedException(Exception):
    def __init__(self) -> None:
        message = f"All registers are closed"
        super().__init__(message)

class AllRegistersOpenException(Exception):
    def __init__(self) -> None:
        message = f"All registers are open"
        super().__init__(message)

class RegisterAlreadyOpenException(Exception):
    def __init__(self) -> None:
        message = f"This Register is already open"
        super().__init__(message)

class RegisterAlreadyClosedException(Exception):
    def __init__(self) -> None:
        message = f"This register is already closed"
        super().__init__(message)

class CannotCloseLastRegisterWithCustomersException(Exception):
    def __init__(self, registerNum: int) -> None:
        self.registerNum = registerNum
        message = f"Can't close register {registerNum}, because it's the last register open and customers are still waiting in the queue"
        super().__init__(message)