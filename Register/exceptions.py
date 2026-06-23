from global_variables import GlobalVariables

class AllRegistersClosedException(Exception):
    def __init__(self) -> None:
        message = f"All registers are closed"
        super().__init__(message)

class AllRegistersOpenException(Exception):
    def __init__(self) -> None:
        message = f"All registers are open"
        super().__init__(message)

class RegisterAlreadyOpenException(Exception):
    def __init__(self, registerNum: int) -> None:
        self.RegisterNum = registerNum
        message = f"Register {registerNum + 1} is already open"
        super().__init__(message)

class RegisterAlreadyClosedException(Exception):
    def __init__(self, registerNum: int) -> None:
        self.RegisterNum = registerNum
        message = f"Register {registerNum + 1} is already closed"
        super().__init__(message)

class CannotCloseLastRegisterWithCustomersException(Exception):
    def __init__(self, registerNum: int) -> None:
        self.RegisterNum = registerNum
        message = f"Can't close register {registerNum + 1}, because it's the last register open and customers are still waiting in the queue"
        super().__init__(message)

class InvalidRegisterNumberException(Exception):
    def __init__(self, registerNum: int) -> None:
        self.RegisterNum = registerNum
        message = f"Entered register number {registerNum} is invalid, the range is between 1 and {GlobalVariables.MaxRegisterAmount}"
        super().__init__(message)