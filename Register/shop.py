from global_variables import GlobalVariables
from exceptions import AllRegistersClosedException, AllRegistersOpenException, RegisterAlreadyOpenException, RegisterAlreadyClosedException
from register import Register

class Shop:
    Registers: list[Register]
    OpenRegisterCount: int

    def __init__(self) -> None:
        self.Registers = [Register() for _ in range(GlobalVariables.RegisterAmount)]
        self.OpenRegisterCount = 0

        for i in range(GlobalVariables.RegisterAmount // 2):
            self.OpenRegister(i)
            self.OpenRegisterCount += 1

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
        register = self.Registers[registerNum]

        if register.IsOpen:
            raise RegisterAlreadyOpenException

        if self.OpenRegisterCount == GlobalVariables.RegisterAmount:
            raise AllRegistersOpenException

        register.Open()
        self.OpenRegisterCount += 1
