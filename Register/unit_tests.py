import unittest
from register import Register
from shop import Shop
from exceptions import AllRegistersClosedException, AllRegistersOpenException, RegisterAlreadyOpenException, RegisterAlreadyClosedException, CannotCloseLastRegisterWithCustomersException, InvalidRegisterNumberException
from global_variables import GlobalVariables


class RegisterTests(unittest.TestCase):
    def setUp(self) -> None:
        self.target = Register()

    def test_Initialization_WhenObjectIsCreated_IsOpenIsFalse(self) -> None:
        self.assertFalse(self.target.IsOpen)

    def test_Initialization_WhenObjectIsCreated_CustomersLengthIs0(self) -> None:
        self.assertEqual(len(self.target.Customers), 0)

    def test_Open_WhenRegisterIsClosed_IsOpenIsTrue(self) -> None:
        self.target.IsOpen = False

        self.target.Open()

        self.assertTrue(self.target.IsOpen)

    def test_Open_WhenRegisterIsOpen_IsOpenIsTrue(self) -> None:
        self.target.IsOpen = True

        self.target.Open()

        self.assertTrue(self.target.IsOpen)

    def test_Close_WhenRegisterIsOpen_IsOpenIsFalse(self) -> None:
        self.target.IsOpen = True

        self.target.Close()

        self.assertFalse(self.target.IsOpen)

    def test_Close_WhenRegisterIsClosed_IsOpenIsFalse(self) -> None:
        self.target.IsOpen = False

        self.target.Close()

        self.assertFalse(self.target.IsOpen)

    def test_AddPerson_WhenRegisterIsClosed_CustomersLengthIs0(self) -> None:
        self.target.IsOpen = False

        self.target.AddPerson("Peter")

        self.assertEqual(0, len(self.target.Customers))

    def test_AddPerson_WhenRegisterIsOpen_CustomersLengthIs1(self) -> None:
        self.target.IsOpen = True

        self.target.AddPerson("Peter")

        self.assertEqual(1, len(self.target.Customers))

    def test_Close_WhenRegisterIsOpenAndHasPeople_CustomersLengthIs0(self) -> None:
        self.target.IsOpen = True
        self.target.Customers.append("Peter")

        self.target.Close()

        self.assertFalse(self.target.IsOpen)
        self.assertEqual(0, len(self.target.Customers))

    def test_Transact_WhenRegisterIsOpenAndHasPeople_CustomerLengthIs0(self) -> None:
        self.target.IsOpen = True
        self.target.Customers.append("Peter")

        self.target.Transact()

        self.assertEqual(0, len(self.target.Customers))

    def test_Transact_WhenRegisterIsOpen_CustomerLengthIs0(self) -> None:
        self.target.IsOpen = True

        self.target.Transact()

        self.assertEqual(0, len(self.target.Customers))

    def test_Transact_WhenRegisterIsClosed_CustomerLengthIs0(self) -> None:
        self.target.IsOpen = False

        self.target.Transact()

        self.assertEqual(0, len(self.target.Customers))


class ShopTests(unittest.TestCase):
    def setUp(self) -> None:
        self.target = Shop()

    def test_Initialization_WhenObjectIsCreated_OpenRegisterCountIs2(self) -> None:
        self.assertEqual(self.target.OpenRegisterCount, GlobalVariables.MaxRegisterAmount // 2)

    def test_Initialization_WhenObjectIsCreated_FirstHalfOfRegistersAreOpen(self) -> None:
        for i in range(GlobalVariables.MaxRegisterAmount // 2):
            self.assertTrue(self.target.Registers[i].IsOpen)

    def test_Initialization_WhenObjectIsCreated_SecondHalfOfRegistersAreClosed(self) -> None:
        for i in range(GlobalVariables.MaxRegisterAmount // 2, GlobalVariables.MaxRegisterAmount):
            self.assertFalse(self.target.Registers[i].IsOpen)

    def test_Initialization_WhenObjectIsCreated_RegistersLengthIs5(self) -> None:
        self.assertEqual(5, len(self.target.Registers))

    def test_Initialization_WhenObjectIsCreated_AllCustomersListsAreEmpty(self) -> None:
        for r in self.target.Registers:
            self.assertEqual(len(r.Customers), 0)

    def test_ValidateRegisterNumber_WhenRegisterNumberIsNegative_RaisesInvalidRegisterNumberException(self) -> None:
        with self.assertRaises(InvalidRegisterNumberException):
            self.target.ValidateRegisterNumber(-5)

    def test_ValidateRegisterNumber_WhenRegisterNumberIsPositiveAndIsLargerThanOrEqualToMaxRegisterAmount_RaisesInvalidRegisterNumberException(self) -> None:
        with self.assertRaises(InvalidRegisterNumberException):
            self.target.ValidateRegisterNumber(999)

    def test_ValidateRegisterNumber_WhenRegisterNumberIsWithin0AndMaxRegisterAmount_DoesNotRaiseException(self) -> None:
        for i in range(GlobalVariables.MaxRegisterAmount):
            self.target.ValidateRegisterNumber(i)

    def test_FindLowestCustomersInRegisters_WhenAllRegistersAreClosed_IndexIsMinus1(self) -> None:
        for i in range(GlobalVariables.MaxRegisterAmount // 2):
            self.target.Registers[i].Close()

        self.target.OpenRegisterCount = 0

        index = self.target.FindLowestCustomersInRegisters()

        self.assertEqual(-1, index)

    def test_FindLowestCustomersInRegisters_WhenRegistersAreOpen_indexIs2(self) -> None:
        for r in self.target.Registers:
            r.Open()

        self.target.Registers[0].AddPerson("1")
        self.target.Registers[1].AddPerson("1")
        self.target.Registers[4].AddPerson("1")
        self.target.OpenRegisterCount = 5

        index = self.target.FindLowestCustomersInRegisters()

        self.assertEqual(2, index)

    def test_FindLowestCustomersInRegisters_WhenSmallestRegisterIsClosed_indexIs3(self) -> None:
        for r in self.target.Registers:
            r.Open()

        self.target.Registers[0].AddPerson("1")
        self.target.Registers[1].AddPerson("1")
        self.target.Registers[2].Close()
        self.target.Registers[4].AddPerson("1")
        self.target.OpenRegisterCount = 4

        index = self.target.FindLowestCustomersInRegisters()

        self.assertEqual(3, index)

    def test_FindLowestCustomersInRegisters_WhenAllRegisterAreOpenAndHavePeople_indexIs0(self) -> None:
        for r in self.target.Registers:
            r.Open()

        self.target.Registers[0].AddPerson("1")
        self.target.Registers[1].AddPerson("1")
        self.target.Registers[2].AddPerson("1")
        self.target.Registers[3].AddPerson("1")
        self.target.Registers[4].AddPerson("1")
        self.target.OpenRegisterCount = 5

        index = self.target.FindLowestCustomersInRegisters()

        self.assertEqual(0, index)

    def test_SearchOpenRegister_WhenAllRegistersAreClosed_ReturnsMinus1(self) -> None:
        for i in range(GlobalVariables.MaxRegisterAmount // 2):
            self.target.CloseRegister(i)

        index = self.target.SearchOpenRegister([i for i in range(GlobalVariables.MaxRegisterAmount)])

        self.assertEqual(index, -1)

    def test_SearchOpenRegister_WhenAllRegistersAreOpen_Returns0(self) -> None:
        for i in range(GlobalVariables.MaxRegisterAmount // 2, GlobalVariables.MaxRegisterAmount):
            self.target.OpenRegister(i)

        index = self.target.SearchOpenRegister([i for i in range(GlobalVariables.MaxRegisterAmount)])

        self.assertEqual(index, 0)

    def test_SearchOpenRegister_When1RegisterIsOpenAndIsNotTheFirst_Returns1(self) -> None:
        self.target.CloseRegister(0)

        index = self.target.SearchOpenRegister([i for i in range(GlobalVariables.MaxRegisterAmount)])

        self.assertEqual(index, 1)

    def test_AddNewCustomer_WhenRegistersAreOpenAndHavePeople_RegisterLengthIs1(self) -> None:
        for r in self.target.Registers:
            r.Open()

        self.target.Registers[0].AddPerson("1")
        self.target.Registers[1].AddPerson("1")
        self.target.Registers[2].AddPerson("1")
        self.target.Registers[4].AddPerson("1")
        self.target.OpenRegisterCount = 5

        self.target.AddNewCustomer("Name")

        self.assertEqual(1, len(self.target.Registers[3].Customers))

    def test_AddNewCustomer_WhenOneRegisterIsClosedAndHavePeople_RegisterLengthIs2(self) -> None:
        for r in self.target.Registers:
            r.Open()

        self.target.Registers[0].AddPerson("1")
        self.target.Registers[1].AddPerson("1")
        self.target.Registers[2].AddPerson("1")
        self.target.Registers[3].Close()
        self.target.Registers[4].AddPerson("1")
        self.target.OpenRegisterCount = 4

        self.target.AddNewCustomer("Name")

        self.assertEqual(2, len(self.target.Registers[0].Customers))

    def test_AddNewCustomer_WhenRegistersAreClosed_RaisesException(self) -> None:
        self.target.Registers[0].Close()
        self.target.Registers[1].Close()
        self.target.Registers[2].Close()
        self.target.Registers[3].Close()
        self.target.Registers[4].Close()
        self.target.OpenRegisterCount = 0

        with self.assertRaises(AllRegistersClosedException):
            self.target.AddNewCustomer("Name")

        self.assertEqual(0, len(self.target.Registers[0].Customers))
        self.assertEqual(0, len(self.target.Registers[1].Customers))
        self.assertEqual(0, len(self.target.Registers[2].Customers))
        self.assertEqual(0, len(self.target.Registers[3].Customers))
        self.assertEqual(0, len(self.target.Registers[4].Customers))

    def test_AddNewCustomer_WhenOneOpenRegisterExists_CustomerIsAdded(self) -> None:
        self.target.CloseRegister(0)
        self.target.AddNewCustomer("Name")

        self.assertEqual(len(self.target.Registers[1].Customers), 1)

    def test_CloseRegister_WhenAllRegistersAreClosed_RaisesRegisterIsAlreadyClosedException(self) -> None:
        with self.assertRaises(RegisterAlreadyClosedException):
            self.target.CloseRegister(4)

    def test_CloseRegister_WhenRegisterHasNoCustomers_OpenRegisterCountIsDecremented(self) -> None:
        self.target.CloseRegister((GlobalVariables.MaxRegisterAmount // 2) - 1)

        self.assertEqual(self.target.OpenRegisterCount, (GlobalVariables.MaxRegisterAmount // 2) - 1)

    def test_CloseRegister_WhenRegisterHasNoCustomers_IsOpenIsFalse(self) -> None:
        self.target.CloseRegister(1)

        self.assertFalse(self.target.Registers[(GlobalVariables.MaxRegisterAmount // 2) + 1].IsOpen)

    def test_CloseRegister_WhenRegisterIsClosedAndHasPeople_OtherRegistersLengthIs1(self) -> None:
        for r in self.target.Registers:
            r.Open()

        self.target.Registers[0].AddPerson("1")
        self.target.Registers[0].AddPerson("2")
        self.target.Registers[0].AddPerson("3")
        self.target.Registers[0].AddPerson("4")
        self.target.OpenRegisterCount = 5

        self.assertEqual(4, len(self.target.Registers[0].Customers))

        self.target.CloseRegister(0)

        self.assertFalse(self.target.Registers[0].IsOpen)
        self.assertEqual(0, len(self.target.Registers[0].Customers))
        self.assertEqual(1, len(self.target.Registers[1].Customers))
        self.assertEqual(1, len(self.target.Registers[2].Customers))
        self.assertEqual(1, len(self.target.Registers[3].Customers))
        self.assertEqual(1, len(self.target.Registers[4].Customers))

    def test_CloseRegister_WhenOneRegisterIsOpenAndHasPeople_RaisesException(self) -> None:
        self.target.Registers[0].AddPerson("1")
        self.target.Registers[0].AddPerson("2")
        self.target.Registers[0].AddPerson("3")
        self.target.Registers[0].AddPerson("4")
        self.target.Registers[1].Close()
        self.target.Registers[2].Close()
        self.target.Registers[3].Close()
        self.target.Registers[4].Close()
        self.target.OpenRegisterCount = 1

        with self.assertRaises(CannotCloseLastRegisterWithCustomersException):
            self.target.CloseRegister(0)

        self.assertTrue(self.target.Registers[0].IsOpen)
        self.assertEqual(4, len(self.target.Registers[0].Customers))

    def test_OpenRegister_WhenAllRegistersAreOpen_RaisesRegisterAlreadyOpenException(self) -> None:
        for r in self.target.Registers:
            r.Open()

        with self.assertRaises(RegisterAlreadyOpenException):
            self.target.OpenRegister(0)

    def test_OpenRegister_WhenRegisterIsClosed_OpenRegisterCountIsIncremented(self) -> None:
        self.target.OpenRegister(GlobalVariables.MaxRegisterAmount // 2)

        self.assertEqual(self.target.OpenRegisterCount, (GlobalVariables.MaxRegisterAmount // 2) + 1)

    def test_OpenRegister_WhenRegisterIsClosed_IsOpenIsTrue(self) -> None:
        self.target.OpenRegister(GlobalVariables.MaxRegisterAmount // 2)

        self.assertTrue(self.target.Registers[GlobalVariables.MaxRegisterAmount // 2])

    # def test_OpenRegister_WhenRegisterIsOpenAndHasPeople_RegistersLengthIs1(self) -> None:
    #     self.target.Registers[0].Open()
    #     self.target.Registers[0].AddPerson("1")
    #     self.target.Registers[0].AddPerson("2")
    #     self.target.Registers[1].Close()
    #     self.target.Registers[2].Close()
    #     self.target.Registers[3].Close()
    #     self.target.Registers[4].Close()

    #     self.target.OpenRegister(1)

    #     self.assertTrue(self.target.Registers[1].IsOpen)
    #     self.assertEqual(1, len(self.target.Registers[0].Customers))
    #     self.assertEqual(1, len(self.target.Registers[1].Customers))


unittest.main()
