REGISTER_AMOUNT = 5


class Register:
    Customers: list[str]
    Number: int
    IsOpen = True

    def __init__(self) -> None:
        self.Customers = []

    def Open(self) -> None:
        self.IsOpen = True

    def Close(self) -> None:
        self.IsOpen = False
        self.Customers.clear()

    def AddPerson(self, name) -> None:
        if self.IsOpen:
            self.Customers.append(name)

    def Transact(self) -> None:
        if len(self.Customers) > 0:
            self.Customers.pop(0)


class Shop:
    Registers: list[Register] = []
