from global_variables import GlobalVariables
from exceptions import AllRegistersClosedException
from register import Register

class Shop:
    Registers: list[Register]

    def __init__(self) -> None:
        self.Registers = [Register() for _ in range(GlobalVariables.RegisterAmount)]

    def FindLowestCustomersInRegisters(self) -> int:
        indexes = [num for num in range(len(self.Registers))]

        indexes.sort(key=lambda i: len(self.Registers[i].Customers))

        return self.SearchOpenRegister(indexes)

    def SearchOpenRegister(self, indexes: list[int]) -> int:
        for i in indexes:
            if self.Registers[i].IsOpen:
                return i

        return -1

    def AddNewCustomer(self, name: str) -> None:
        i = self.FindLowestCustomersInRegisters()

        if i == -1:
            raise AllRegistersClosedException

        self.Registers[i].AddPerson(name)

    def CloseRegister(self, registerNum: int) -> None:
        openRegisters = 0

        for register in self.Registers:
            if register.IsOpen:
                openRegisters += 1

        if len(self.Registers[registerNum].Customers) > 0 and openRegisters > 1:
            customers: list[str] = self.Registers[registerNum].Customers
            self.Registers[registerNum].Close()

            while len(customers) > 0:
                self.AddNewCustomer(customers.pop())
        elif len(self.Registers[registerNum].Customers) == 0:
            self.Registers[registerNum].Close()
        else:
            raise AllRegistersClosedException

    def OpenRegister(self, registerNum: int) -> None:
        self.Registers[registerNum].Open()