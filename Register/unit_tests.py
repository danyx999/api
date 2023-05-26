import unittest
from register import Register, Shop, AllRegistersClosedException


class RegisterTests(unittest.TestCase):
    def setUp(self) -> None:
        self.target = Register()

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

    def test_WhenObjectIsCreated_RegistersLengthIs5(self) -> None:
        self.assertEqual(5, len(self.target.Registers))

    def test_FindLowestCustomersInRegisters_WhenRegistersAreOpen_indexIs2(self) -> None:
        self.target.Registers[0].AddPerson("1")
        self.target.Registers[1].AddPerson("1")
        self.target.Registers[4].AddPerson("1")

        index = self.target.FindLowestCustomersInRegisters()

        self.assertEqual(2, index)

    def test_FindLowestCustomersInRegisters_WhenSmallestRegisterIsClosed_indexIs3(
        self,
    ) -> None:
        self.target.Registers[0].AddPerson("1")
        self.target.Registers[1].AddPerson("1")
        self.target.Registers[2].Close()
        self.target.Registers[4].AddPerson("1")

        index = self.target.FindLowestCustomersInRegisters()

        self.assertEqual(3, index)

    def test_AddNewCustomer_WhenRegistersAreOpenAndHavePeople_RegisterLengthIs1(
        self,
    ) -> None:
        self.target.Registers[0].AddPerson("1")
        self.target.Registers[1].AddPerson("1")
        self.target.Registers[2].AddPerson("1")
        self.target.Registers[4].AddPerson("1")

        self.target.AddNewCustomer("Name")

        self.assertEqual(1, len(self.target.Registers[3].Customers))

    def test_AddNewCustomer_WhenOneRegisterIsClosedAndHavePeople_RegisterLengthIs2(
        self,
    ) -> None:
        self.target.Registers[0].AddPerson("1")
        self.target.Registers[1].AddPerson("1")
        self.target.Registers[2].AddPerson("1")
        self.target.Registers[3].Close()
        self.target.Registers[4].AddPerson("1")

        self.target.AddNewCustomer("Name")

        self.assertEqual(2, len(self.target.Registers[0].Customers))

    def test_AddNewCustomer_WhenRegistersAreClosed_RaisesException(self) -> None:
        self.target.Registers[0].Close()
        self.target.Registers[1].Close()
        self.target.Registers[2].Close()
        self.target.Registers[3].Close()
        self.target.Registers[4].Close()

        with self.assertRaises(AllRegistersClosedException):
            self.target.AddNewCustomer("Name")
        self.assertEqual(0, len(self.target.Registers[0].Customers))
        self.assertEqual(0, len(self.target.Registers[1].Customers))
        self.assertEqual(0, len(self.target.Registers[2].Customers))
        self.assertEqual(0, len(self.target.Registers[3].Customers))
        self.assertEqual(0, len(self.target.Registers[4].Customers))

    def test_CloseRegister_WhenRegisterIsClosedAndHasPeople_OtherRegistersLengthIs1(
        self,
    ) -> None:
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

    def test_CloseRegister_WhenOneRegisterIsOpenAndHasPeople_RaisesException(
        self,
    ) -> None:
        self.target.Registers[0].AddPerson("1")
        self.target.Registers[0].AddPerson("2")
        self.target.Registers[0].AddPerson("3")
        self.target.Registers[0].AddPerson("4")
        self.target.Registers[1].Close()
        self.target.Registers[2].Close()
        self.target.Registers[3].Close()
        self.target.Registers[4].Close()

        with self.assertRaises(AllRegistersClosedException):
            self.target.CloseRegister(0)
        self.assertTrue(self.target.Registers[0].IsOpen)
        self.assertEqual(4, len(self.target.Registers[0].Customers))


unittest.main()
