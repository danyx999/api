from global_variables import GlobalVariables
from exceptions import AllRegistersClosedException, RegisterAlreadyOpenException, RegisterAlreadyClosedException, CannotCloseLastRegisterWithCustomersException, InvalidRegisterNumberException, RegisterIsClosedException, NoCustomersInRegisterException
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
        if registerNum < 0 or registerNum >= GlobalVariables.MaxRegisterAmount:
            raise InvalidRegisterNumberException(registerNum)

    def FindLowestAndHighestCustomerAmountInRegisters(self) -> tuple[int, int]:
        if self.OpenRegisterCount == 0:
            return (-1, -1)

        indexes = [index for index in range(len(self.Registers)) if self.Registers[index].IsOpen]

        indexes.sort(key=lambda i: len(self.Registers[i].Customers))

        return (indexes[0], indexes[-1])

    def AddNewCustomer(self, name: str) -> None:
        i, _ = self.FindLowestAndHighestCustomerAmountInRegisters()

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

    def BalanceCustomers(self) -> None:
        while True:
            low, high = self.FindLowestAndHighestCustomerAmountInRegisters()

            if len(self.Registers[high].Customers) - len(self.Registers[low].Customers) <= 1:
                break

            customer = self.Registers[high].Customers.pop()
            self.Registers[low].AddPerson(customer)

    def OpenRegister(self, registerNum: int) -> None:
        self.ValidateRegisterNumber(registerNum)

        register = self.Registers[registerNum]

        if register.IsOpen:
            raise RegisterAlreadyOpenException(registerNum)

        register.Open()
        self.OpenRegisterCount += 1
        self.BalanceCustomers()

    def ServeCustomer(self, registerNum: int) -> None:
        self.ValidateRegisterNumber(registerNum)

        register = self.Registers[registerNum]

        if not register.IsOpen:
            raise RegisterIsClosedException(registerNum)

        if len(register.Customers) == 0:
            raise NoCustomersInRegisterException(registerNum)

        register.Serve()
