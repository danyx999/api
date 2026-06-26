import unittest
from register import Register
from shop import Shop
from exceptions import AllRegistersClosedException, RegisterAlreadyOpenException, RegisterAlreadyClosedException, CannotCloseLastRegisterWithCustomersException, InvalidRegisterNumberException, RegisterIsClosedException, NoCustomersInRegisterException
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

        self.target.Serve()

        self.assertEqual(0, len(self.target.Customers))

    def test_Transact_WhenRegisterIsOpen_CustomerLengthIs0(self) -> None:
        self.target.IsOpen = True

        self.target.Serve()

        self.assertEqual(0, len(self.target.Customers))

    def test_Transact_WhenRegisterIsClosed_CustomerLengthIs0(self) -> None:
        self.target.IsOpen = False

        self.target.Serve()

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

    def test_FindLowestAndHighestCustomerAmountInRegisters_WhenAllRegistersAreClosed_LowestANdHighestAreMinus1(self) -> None:
        for i in range(GlobalVariables.MaxRegisterAmount // 2):
            self.target.CloseRegister(i)

        low, high = self.target.FindLowestAndHighestCustomerAmountInRegisters()

        self.assertEqual(-1, low)
        self.assertEqual(-1, high)

    def test_FindLowestAndHighestCustomerAmountInRegisters_WhenRegistersAreOpen_LowIs2(self) -> None:
        for i in range(GlobalVariables.MaxRegisterAmount // 2, GlobalVariables.MaxRegisterAmount):
            self.target.OpenRegister(i)

        self.target.Registers[0].AddPerson("1")
        self.target.Registers[1].AddPerson("1")
        self.target.Registers[4].AddPerson("1")

        index, _ = self.target.FindLowestAndHighestCustomerAmountInRegisters()

        self.assertEqual(2, index)

    def test_FindLowestAndHighestCustomerAmountInRegisters_WhenSmallestRegisterIsClosed_LowIs3(self) -> None:
        for i in range(GlobalVariables.MaxRegisterAmount // 2, GlobalVariables.MaxRegisterAmount):
            self.target.OpenRegister(i)

        self.target.Registers[0].AddPerson("1")
        self.target.Registers[1].AddPerson("1")
        self.target.CloseRegister(2)
        self.target.Registers[4].AddPerson("1")

        index, _ = self.target.FindLowestAndHighestCustomerAmountInRegisters()

        self.assertEqual(3, index)

    def test_FindLowestAndHighestCustomerAmountInRegisters_WhenAllRegisterAreOpenAndHavePeople_LowIs0(self) -> None:
        for i in range(GlobalVariables.MaxRegisterAmount // 2, GlobalVariables.MaxRegisterAmount):
            self.target.OpenRegister(i)

        self.target.Registers[0].AddPerson("1")
        self.target.Registers[1].AddPerson("1")
        self.target.Registers[2].AddPerson("1")
        self.target.Registers[3].AddPerson("1")
        self.target.Registers[4].AddPerson("1")

        index, _ = self.target.FindLowestAndHighestCustomerAmountInRegisters()

        self.assertEqual(0, index)

    def test_FindLowestAndHighestCustomerAmountInRegisters_WhenRegistersAreOpen_HighIs4(self) -> None:
        for i in range(GlobalVariables.MaxRegisterAmount // 2, GlobalVariables.MaxRegisterAmount):
            self.target.OpenRegister(i)

        self.target.Registers[0].AddPerson("1")
        self.target.Registers[1].AddPerson("1")
        self.target.Registers[4].AddPerson("1")

        _, index = self.target.FindLowestAndHighestCustomerAmountInRegisters()

        self.assertEqual(4, index)

    def test_FindLowestAndHighestCustomerAmountInRegisters_WhenHighestRegisterIsFirst_HighIs0(self) -> None:
        for i in range(GlobalVariables.MaxRegisterAmount // 2, GlobalVariables.MaxRegisterAmount):
            self.target.OpenRegister(i)

        self.target.Registers[0].AddPerson("1")
        self.target.Registers[0].AddPerson("1")
        self.target.Registers[1].AddPerson("1")
        self.target.CloseRegister(2)
        self.target.Registers[4].AddPerson("1")

        _, index = self.target.FindLowestAndHighestCustomerAmountInRegisters()

        self.assertEqual(0, index)

    def test_FindLowestAndHighestCustomerAmountInRegisters_WhenAllRegisterAreOpenAndHavePeople_HighIs4(self) -> None:
        for i in range(GlobalVariables.MaxRegisterAmount // 2, GlobalVariables.MaxRegisterAmount):
            self.target.OpenRegister(i)

        self.target.Registers[0].AddPerson("1")
        self.target.Registers[1].AddPerson("1")
        self.target.Registers[2].AddPerson("1")
        self.target.Registers[3].AddPerson("1")
        self.target.Registers[4].AddPerson("1")

        _, index= self.target.FindLowestAndHighestCustomerAmountInRegisters()

        self.assertEqual(4, index)

    def test_AddNewCustomer_WhenRegistersAreOpenAndHavePeople_RegisterLengthIs1(self) -> None:
        for i in range(GlobalVariables.MaxRegisterAmount // 2, GlobalVariables.MaxRegisterAmount):
            self.target.OpenRegister(i)

        self.target.Registers[0].AddPerson("1")
        self.target.Registers[1].AddPerson("1")
        self.target.Registers[2].AddPerson("1")
        self.target.Registers[4].AddPerson("1")

        self.target.AddNewCustomer("Name")

        self.assertEqual(1, len(self.target.Registers[3].Customers))

    def test_AddNewCustomer_WhenOneRegisterIsClosedAndHavePeople_RegisterLengthIs2(self) -> None:
        for i in range(GlobalVariables.MaxRegisterAmount // 2, GlobalVariables.MaxRegisterAmount):
            self.target.OpenRegister(i)

        self.target.Registers[0].AddPerson("1")
        self.target.Registers[1].AddPerson("1")
        self.target.Registers[2].AddPerson("1")
        self.target.Registers[3].Close()
        self.target.Registers[4].AddPerson("1")

        self.target.AddNewCustomer("Name")

        self.assertEqual(2, len(self.target.Registers[0].Customers))

    def test_AddNewCustomer_WhenRegistersAreClosed_RaisesException(self) -> None:
        for i in range(GlobalVariables.MaxRegisterAmount // 2):
            self.target.CloseRegister(i)

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

    def test_RedistributeCustomers_When2RegistersAreOpenAndClosedAnd2CustomersAreRedistributed_BothOpenRegistersHave1Customer(self) -> None:
        self.target.RedistributeCustomers(["1" for _ in range(GlobalVariables.MaxRegisterAmount // 2)])

        for i in range(GlobalVariables.MaxRegisterAmount // 2):
            self.assertEqual(len(self.target.Registers[i].Customers), 1)

    def test_RedistributeCustomers_WhenAllRegistersAreOpenAnd5CustomersAreRedistributed_AllRegistersHave1Customer(self) -> None:
        for i in range(GlobalVariables.MaxRegisterAmount // 2, GlobalVariables.MaxRegisterAmount):
            self.target.OpenRegister(i)

        self.target.RedistributeCustomers(["1" for _ in range(GlobalVariables.MaxRegisterAmount)])

        for i in range(GlobalVariables.MaxRegisterAmount):
            self.assertEqual(len(self.target.Registers[i].Customers), 1)

    def test_CloseRegister_WhenAllRegistersAreClosed_RaisesRegisterIsAlreadyClosedException(self) -> None:
        with self.assertRaises(RegisterAlreadyClosedException):
            self.target.CloseRegister(GlobalVariables.MaxRegisterAmount - 1)

    def test_CloseRegister_WhenRegisterHasNoCustomers_OpenRegisterCountIsDecremented(self) -> None:
        self.target.CloseRegister((GlobalVariables.MaxRegisterAmount // 2) - 1)

        self.assertEqual(self.target.OpenRegisterCount, (GlobalVariables.MaxRegisterAmount // 2) - 1)

    def test_CloseRegister_WhenRegisterHasNoCustomers_IsOpenIsFalse(self) -> None:
        self.target.CloseRegister(1)

        self.assertFalse(self.target.Registers[(GlobalVariables.MaxRegisterAmount // 2) - 1].IsOpen)

    def test_CloseRegister_WhenRegisterIsAlreadyClosed_RaisesRegisterAlreadyClosedException(self) -> None:
        with self.assertRaises(RegisterAlreadyClosedException):
            self.target.CloseRegister(GlobalVariables.MaxRegisterAmount - 1)

    def test_CloseRegister_WhenRegisterNumberIsNegative_RaisesInvalidRegisterNumberException(self) -> None:
        with self.assertRaises(InvalidRegisterNumberException):
            self.target.CloseRegister(-5)

    def test_CloseRegister_WhenRegisterNumberIsOutOfRange_RaisesInvalidRegisterNumberException(self) -> None:
        with self.assertRaises(InvalidRegisterNumberException):
            self.target.CloseRegister(999)

    def test_CloseRegister_WhenRegisterIsClosedAndHasPeople_OtherRegistersLengthIs1(self) -> None:
        for i in range(GlobalVariables.MaxRegisterAmount // 2, GlobalVariables.MaxRegisterAmount):
            self.target.OpenRegister(i)

        self.target.Registers[0].AddPerson("1")
        self.target.Registers[0].AddPerson("2")
        self.target.Registers[0].AddPerson("3")
        self.target.Registers[0].AddPerson("4")

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

        self.target.CloseRegister(1)

        with self.assertRaises(CannotCloseLastRegisterWithCustomersException):
            self.target.CloseRegister(0)

        self.assertTrue(self.target.Registers[0].IsOpen)
        self.assertEqual(4, len(self.target.Registers[0].Customers))

    def test_BalanceCustomers_When1RegisterIsOpenAndHasNoCustomers_NothingHappens(self) -> None:
        self.target.CloseRegister(1)

        self.target.BalanceCustomers()

        self.assertEqual(self.target.Registers[0].Customers, [])

    def test_BalanceCustomers_When1RegisterIsOpenAndHas1Customer_NothingHappens(self) -> None:
        self.target.CloseRegister(1)
        self.target.Registers[0].AddPerson("Name")

        self.target.BalanceCustomers()

        self.assertEqual(self.target.Registers[0].Customers, ["Name"])

    def test_BalanceCustomers_When1RegisterIsOpenAndHasManyCustomers_NothingHappens(self) -> None:
        self.target.CloseRegister(1)

        customers = [str(n) for n in range(5)]

        for c in customers:
            self.target.Registers[0].AddPerson(c)

        self.target.BalanceCustomers()

        self.assertEqual(self.target.Registers[0].Customers, customers)

    def test_BalanceCustomers_When2RegistersAreOpenAndAreAlreadyBalancedAndHasNoCustomers_NothingHappens(self) -> None:
        self.target.BalanceCustomers()

        for i in range(2):
            self.assertEqual(self.target.Registers[i].Customers, [])

    def test_BalanceCustomers_When2RegistersAreOpenAndAreAlreadyBalancedAndCustomersAreEven_NothingHappens(self) -> None:
        customers1 = [str(c) for c in range(2)]
        customers2 = [str(c) for c in range(2)]

        for c1, c2 in zip(customers1, customers2):
            self.target.Registers[0].AddPerson(c1)
            self.target.Registers[1].AddPerson(c2)

        self.target.BalanceCustomers()

        self.assertEqual(self.target.Registers[0].Customers, customers1)
        self.assertEqual(self.target.Registers[1].Customers, customers2)

    def test_BalanceCustomers_When2RegistersAreOpenAndAreAlreadyBalancedAndCustomersAreOdd_NothingHappens(self) -> None:
        customers1 = [str(c) for c in range(2)]
        customers2 = [str(c) for c in range(3)]

        for c1 in customers1:
            self.target.Registers[0].AddPerson(c1)

        for c2 in customers2:
            self.target.Registers[1].AddPerson(c2)

        self.target.BalanceCustomers()

        self.assertEqual(self.target.Registers[0].Customers, customers1)
        self.assertEqual(self.target.Registers[1].Customers, customers2)

    def test_BalanceCustomers_When2RegistersAreOpenAndRegisterHasEvenCustomers_RegistersBecomeBalanced(self) -> None:
        customers = [str(c) for c in range(4)]

        for c in customers:
            self.target.Registers[0].AddPerson(c)

        self.target.BalanceCustomers()

        sizes = [len(r.Customers) for r in self.target.Registers if r.IsOpen]

        self.assertEqual(sum(sizes), len(customers))
        self.assertLessEqual(max(sizes) - min(sizes), 1)

    def test_BalanceCustomers_When2RegistersAreOpenAndRegisterHasOddCustomers_RegistersBecomeBalanced(self) -> None:
        customers = [str(c) for c in range(5)]

        for c in customers:
            self.target.Registers[0].AddPerson(c)

        self.target.BalanceCustomers()

        sizes = [len(r.Customers) for r in self.target.Registers if r.IsOpen]

        self.assertEqual(sum(sizes), len(customers))
        self.assertLessEqual(max(sizes) - min(sizes), 1)

    def test_BalanceCustomers_When3RegistersAreOpenAndAreAlreadyBalancedHasNoCustomers_NothingHappens(self) -> None:
        self.target.OpenRegister(2)

        self.target.BalanceCustomers()

        for i in range(3):
            self.assertEqual(self.target.Registers[i].Customers, [])

    def test_BalanceCustomers_When3RegistersAreOpenAndAreAlreadyBalancedAndCustomersAreEven_NothingHappens(self) -> None:
        customers1 = [str(c) for c in range(3)]
        customers2 = [str(c) for c in range(3)]
        customers3 = [str(c) for c in range(2)]

        self.target.OpenRegister(2)

        for c1, c2 in zip(customers1, customers2):
            self.target.Registers[0].AddPerson(c1)
            self.target.Registers[1].AddPerson(c2)

        for c3 in customers3:
            self.target.Registers[2].AddPerson(c3)

        self.target.BalanceCustomers()

        self.assertEqual(self.target.Registers[0].Customers, customers1)
        self.assertEqual(self.target.Registers[1].Customers, customers2)
        self.assertEqual(self.target.Registers[2].Customers, customers3)

    def test_BalanceCustomers_When3RegistersAreOpenAndAreAlreadyBalancedAndCustomersAreOdd_NothingHappens(self) -> None:
        customers1 = [str(c) for c in range(2)]
        customers2 = [str(c) for c in range(2)]
        customers3 = [str(c) for c in range(3)]

        self.target.OpenRegister(2)

        for c1, c2 in zip(customers1, customers2):
            self.target.Registers[0].AddPerson(c1)
            self.target.Registers[1].AddPerson(c2)

        for c3 in customers3:
            self.target.Registers[2].AddPerson(c3)

        self.target.BalanceCustomers()

        self.assertEqual(self.target.Registers[0].Customers, customers1)
        self.assertEqual(self.target.Registers[1].Customers, customers2)
        self.assertEqual(self.target.Registers[2].Customers, customers3)

    def test_BalanceCustomers_When3RegistersAreOpenAndRegisterHasEvenCustomers_RegistersBecomeBalanced(self) -> None:
        customers = [str(c) for c in range(6)]

        for c in customers:
            self.target.Registers[0].AddPerson(c)

        self.target.OpenRegister(2)

        self.target.BalanceCustomers()

        sizes = [len(r.Customers) for r in self.target.Registers if r.IsOpen]

        self.assertEqual(sum(sizes), len(customers))
        self.assertLessEqual(max(sizes) - min(sizes), 1)

    def test_BalanceCustomers_When3RegistersAreOpenAndRegisterHasOddCustomers_RegistersBecomeBalanced(self) -> None:
        customers = [str(c) for c in range(7)]

        for c in customers:
            self.target.Registers[0].AddPerson(c)

        self.target.OpenRegister(2)

        self.target.BalanceCustomers()

        sizes = [len(r.Customers) for r in self.target.Registers if r.IsOpen]

        self.assertEqual(sum(sizes), len(customers))
        self.assertLessEqual(max(sizes) - min(sizes), 1)

    def test_BalanceCustomers_WhenAllRegistersAreOpenAndAreAlreadyBalancedAndHasNoCustomers_NothingHappens(self) -> None:
        for i in range(GlobalVariables.MaxRegisterAmount // 2, GlobalVariables.MaxRegisterAmount):
            self.target.OpenRegister(i)

        self.target.BalanceCustomers()

        for i in range(GlobalVariables.MaxRegisterAmount):
            self.assertEqual(self.target.Registers[i].Customers, [])

    def test_BalanceCustomers_WhenAllRegistersAreOpenAndAreAlreadyBalancedAndCustomersAreEven_NothingHappens(self) -> None:
        customers1 = [str(c) for c in range(3)]
        customers2 = [str(c) for c in range(3)]
        customers3 = [str(c) for c in range(2)]
        customers4 = [str(c) for c in range(3)]
        customers5 = [str(c) for c in range(3)]

        for i in range(GlobalVariables.MaxRegisterAmount // 2, GlobalVariables.MaxRegisterAmount):
            self.target.OpenRegister(i)

        for c1, c2, c4, c5 in zip(customers1, customers2, customers4, customers5):
            self.target.Registers[0].AddPerson(c1)
            self.target.Registers[1].AddPerson(c2)
            self.target.Registers[3].AddPerson(c4)
            self.target.Registers[4].AddPerson(c5)

        for c3 in customers3:
            self.target.Registers[2].AddPerson(c3)

        self.target.BalanceCustomers()

        self.assertEqual(self.target.Registers[0].Customers, customers1)
        self.assertEqual(self.target.Registers[1].Customers, customers2)
        self.assertEqual(self.target.Registers[2].Customers, customers3)
        self.assertEqual(self.target.Registers[3].Customers, customers4)
        self.assertEqual(self.target.Registers[4].Customers, customers5)

    def test_BalanceCustomers_WhenAllRegistersAreOpenAndAreAlreadyBalancedAndCustomersAreOdd_NothingHappens(self) -> None:
        customers1 = [str(c) for c in range(2)]
        customers2 = [str(c) for c in range(3)]
        customers3 = [str(c) for c in range(3)]
        customers4 = [str(c) for c in range(2)]
        customers5 = [str(c) for c in range(3)]

        for i in range(GlobalVariables.MaxRegisterAmount // 2, GlobalVariables.MaxRegisterAmount):
            self.target.OpenRegister(i)

        for c1, c4 in zip(customers1, customers4):
            self.target.Registers[0].AddPerson(c1)
            self.target.Registers[3].AddPerson(c4)

        for c2, c3, c5 in zip(customers2, customers3, customers5):
            self.target.Registers[1].AddPerson(c2)
            self.target.Registers[2].AddPerson(c3)
            self.target.Registers[4].AddPerson(c5)

        self.target.BalanceCustomers()

        self.assertEqual(self.target.Registers[0].Customers, customers1)
        self.assertEqual(self.target.Registers[1].Customers, customers2)
        self.assertEqual(self.target.Registers[2].Customers, customers3)
        self.assertEqual(self.target.Registers[3].Customers, customers4)
        self.assertEqual(self.target.Registers[4].Customers, customers5)

    def test_BalanceCustomers_WhenAllRegistersAreOpenAndRegisterHasEvenCustomers_RegistersBecomeBalanced(self) -> None:
        customers = [str(c) for c in range(10)]

        for c in customers:
            self.target.Registers[0].AddPerson(c)

        for i in range(GlobalVariables.MaxRegisterAmount // 2, GlobalVariables.MaxRegisterAmount):
            self.target.OpenRegister(i)

        self.target.BalanceCustomers()

        sizes = [len(r.Customers) for r in self.target.Registers if r.IsOpen]

        self.assertEqual(sum(sizes), len(customers))
        self.assertLessEqual(max(sizes) - min(sizes), 1)

    def test_BalanceCustomers_WhenAllRegistersAreOpenAndRegisterHasOddCustomers_RegistersBecomeBalanced(self) -> None:
        customers = [str(c) for c in range(13)]

        for c in customers:
            self.target.Registers[0].AddPerson(c)

        for i in range(GlobalVariables.MaxRegisterAmount // 2, GlobalVariables.MaxRegisterAmount):
            self.target.OpenRegister(i)

        self.target.BalanceCustomers()

        sizes = [len(r.Customers) for r in self.target.Registers if r.IsOpen]

        self.assertEqual(sum(sizes), len(customers))
        self.assertLessEqual(max(sizes) - min(sizes), 1)

    def test_OpenRegister_WhenAllRegistersAreOpen_RaisesRegisterAlreadyOpenException(self) -> None:
        for i in range(GlobalVariables.MaxRegisterAmount // 2, GlobalVariables.MaxRegisterAmount):
            self.target.OpenRegister(i)

        with self.assertRaises(RegisterAlreadyOpenException):
            self.target.OpenRegister(0)

    def test_OpenRegister_WhenRegisterIsClosed_OpenRegisterCountIsIncremented(self) -> None:
        self.target.OpenRegister(GlobalVariables.MaxRegisterAmount // 2)

        self.assertEqual(self.target.OpenRegisterCount, (GlobalVariables.MaxRegisterAmount // 2) + 1)

    def test_OpenRegister_WhenRegisterIsClosed_IsOpenIsTrue(self) -> None:
        self.target.OpenRegister(GlobalVariables.MaxRegisterAmount // 2)

        self.assertTrue(self.target.Registers[GlobalVariables.MaxRegisterAmount // 2].IsOpen)

    def test_OpenRegister_WhenRegisterIsAlreadyOpen_RaisesRegisterAlreadyOpenException(self) -> None:
        with self.assertRaises(RegisterAlreadyOpenException):
            self.target.OpenRegister(0)

    def test_OpenRegister_WhenRegisterNumberIsNegative_RaisesInvalidRegisterNumberException(self) -> None:
        with self.assertRaises(InvalidRegisterNumberException):
            self.target.OpenRegister(-5)

    def test_OpenRegister_WhenRegisterNumberIsOutOfRange_RaisesInvalidRegisterNumberException(self) -> None:
        with self.assertRaises(InvalidRegisterNumberException):
            self.target.OpenRegister(999)

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

    def test_ServeCustomer_WhenRegisterNumberIsNegative_RaisesInvalidRegisterNumberException(self) -> None:
        with self.assertRaises(InvalidRegisterNumberException):
            self.target.ServeCustomer(-5)

    def test_ServeCustomer_WhenRegisterNumberIsOutOfRange_RaisesInvalidRegisterNumberException(self) -> None:
        with self.assertRaises(InvalidRegisterNumberException):
            self.target.ServeCustomer(999)

    def test_ServeCustomer_WhenRegisterIsClosed_RaisesRegisterIsClosedException(self) -> None:
        with self.assertRaises(RegisterIsClosedException):
            self.target.ServeCustomer(GlobalVariables.MaxRegisterAmount - 1)

    def test_ServeCustomer_WhenRegisterIsEmpty_RaisesNoCustomersInRegisterException(self) -> None:
        with self.assertRaises(NoCustomersInRegisterException):
            self.target.ServeCustomer(0)

    def test_ServeCustomer_WhenRegisterIsEmpty_RegisterWillNotChange(self) -> None:
        with self.assertRaises(NoCustomersInRegisterException):
            self.target.ServeCustomer(0)

        self.assertEqual(len(self.target.Registers[0].Customers), 0)

    def test_ServeCustomer_WhenRegisterHas1Customer_CustomerLengthIs0(self) -> None:
        self.target.AddNewCustomer("Name")

        self.target.ServeCustomer(0)

        self.assertEqual(len(self.target.Registers[0].Customers), 0)

    def test_ServeCustomer_WhenRegisterHas4Customers_CustomerLengthIs3(self) -> None:
        customers = ["A", "B", "C", "D"]

        self.target.CloseRegister(1)

        for c in customers:
            self.target.AddNewCustomer(c)

        self.target.ServeCustomer(0)

        self.assertEqual(len(self.target.Registers[0].Customers), 3)

    def test_ServeCustomer_WhenRegisterHas4Customers_RegisterHasCorrectOrder(self) -> None:
        customers = ["A", "B", "C", "D"]
        expected_customers = ["B", "C", "D"]

        self.target.CloseRegister(1)

        for c in customers:
            self.target.AddNewCustomer(c)

        self.target.ServeCustomer(0)

        self.assertEqual(self.target.Registers[0].Customers, expected_customers)

    def test_ServeCustomer_WhenRegisterHas4CustomersAndServes2Customers_CustomerLengthIs2(self) -> None:
        customers = ["A", "B", "C", "D"]

        self.target.CloseRegister(1)

        for c in customers:
            self.target.AddNewCustomer(c)

        for _ in range(2):
            self.target.ServeCustomer(0)

        self.assertEqual(len(self.target.Registers[0].Customers), 2)

    def test_ServeCustomer_WhenRegisterHas4CustomersAndServes2Customers_RegisterHasCorrectOrder(self) -> None:
        customers = ["A", "B", "C", "D"]
        expected_customers = ["C", "D"]

        self.target.CloseRegister(1)

        for c in customers:
            self.target.AddNewCustomer(c)

        for _ in range(2):
            self.target.ServeCustomer(0)

        self.assertEqual(self.target.Registers[0].Customers, expected_customers)

    def test_ServeCustomer_WhenRegisterHas4CustomersAndServesAllCustomers_RegisterIsEmpty(self) -> None:
        customers = ["A", "B", "C", "D"]

        self.target.CloseRegister(1)

        for c in customers:
            self.target.AddNewCustomer(c)

        for _ in range(4):
            self.target.ServeCustomer(0)

        self.assertEqual(len(self.target.Registers[0].Customers), 0)


unittest.main()
