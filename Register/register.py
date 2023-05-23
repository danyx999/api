from global_variables import GlobalVariables


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
        if len(self.Customers) > 0 and self.IsOpen:
            self.Customers.pop(0)


class Shop:
    Registers: list[Register]

    def __init__(self) -> None:
        self.Registers = [Register() for _ in range(GlobalVariables.RegisterAmount)]

    def FindLowestCustomersInRegisters(self) -> int:
        indexes = [num for num in range(len(self.Registers))]

        indexes.sort(key=lambda i: len(self.Registers[i].Customers))

        for i in indexes:
            if self.Registers[i].IsOpen:
                return i

    def AddNewCustomer(self, name) -> None:
        self.Registers[self.FindLowestCustomersInRegisters()].AddPerson(name)
