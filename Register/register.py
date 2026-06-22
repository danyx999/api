class Register:
    Customers: list[str]
    IsOpen = True

    def __init__(self) -> None:
        self.Customers = []

    def Open(self) -> None:
        self.IsOpen = True

    def Close(self) -> None:
        self.IsOpen = False
        self.Customers.clear()

    def AddPerson(self, name: str) -> None:
        if self.IsOpen:
            self.Customers.append(name)

    def Transact(self) -> None:
        if len(self.Customers) > 0 and self.IsOpen:
            self.Customers.pop(0)