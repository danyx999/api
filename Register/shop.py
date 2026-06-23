from global_variables import GlobalVariables
from exceptions import AllRegistersClosedException, AllRegistersOpenException, RegisterAlreadyOpenException, RegisterAlreadyClosedException, CannotCloseLastRegisterWithCustomersException, InvalidRegisterNumberException
from register import Register

class Shop:
    Registers: list[Register]
    OpenRegisterCount: int

    def __init__(self) -> None:
        self.Registers = [Register() for _ in range(GlobalVariables.MaxRegisterAmount)]
        self.OpenRegisterCount = 0

        for i in range(GlobalVariables.MaxRegisterAmount // 2):
            self.OpenRegister(i)

    def ValidateRegisterNumber(self, registerNum: int) -> None:
        if GlobalVariables.MaxRegisterAmount <= registerNum < 0:
            raise InvalidRegisterNumberException(registerNum)

    def FindLowestCustomersInRegisters(self) -> int:
        indexes = [index for index in range(len(self.Registers))]

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

    def RedistributeCustomers(self, customers: list[str]) -> None:
        while len(customers) > 0:
            self.AddNewCustomer(customers.pop())

    def CloseRegister(self, registerNum: int) -> None:
        self.ValidateRegisterNumber(registerNum)

        register = self.Registers[registerNum]

        if not register.IsOpen:
            raise RegisterAlreadyClosedException(registerNum)

        if self.OpenRegisterCount == 1 and len(register.Customers) > 0:
            raise CannotCloseLastRegisterWithCustomersException(registerNum)

        customers = register.Customers.copy()

        register.Close()
        self.OpenRegisterCount -= 1

        self.RedistributeCustomers(customers)

    def OpenRegister(self, registerNum: int) -> None:
        self.ValidateRegisterNumber(registerNum)

        register = self.Registers[registerNum]

        if register.IsOpen:
            raise RegisterAlreadyOpenException(registerNum)

        if self.OpenRegisterCount == GlobalVariables.MaxRegisterAmount:
            raise AllRegistersOpenException

        register.Open()
        self.OpenRegisterCount += 1
