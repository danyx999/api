import unittest
from register import Register, Shop


class RegisterTests(unittest.TestCase):
    def test_Open_WhenRegisterIsClosed_IsOpenIsTrue(self) -> None:
        target = Register()
        target.IsOpen = False

        target.Open()

        self.assertTrue(target.IsOpen)

    def test_Open_WhenRegisterIsOpen_IsOpenIsTrue(self) -> None:
        target = Register()
        target.IsOpen = True

        target.Open()

        self.assertTrue(target.IsOpen)

    def test_Close_WhenRegisterIsOpen_IsOpenIsFalse(self) -> None:
        target = Register()
        target.IsOpen = True

        target.Close()

        self.assertFalse(target.IsOpen)

    def test_Close_WhenRegisterIsClosed_IsOpenIsFalse(self) -> None:
        target = Register()
        target.IsOpen = False

        target.Close()

        self.assertFalse(target.IsOpen)

    def test_AddPerson_WhenRegisterIsClosed_CustomersLengthIs0(self) -> None:
        target = Register()
        target.IsOpen = False

        target.AddPerson("Peter")

        self.assertEqual(0, len(target.Customers))

    def test_AddPerson_WhenRegisterIsOpen_CustomersLengthIs1(self) -> None:
        target = Register()
        target.IsOpen = True

        target.AddPerson("Peter")

        self.assertEqual(1, len(target.Customers))

    def test_Close_WhenRegisterIsOpenAndHasPeople_CustomersLengthIs0(self) -> None:
        target = Register()
        target.IsOpen = True
        target.Customers.append("Peter")

        target.Close()

        self.assertFalse(target.IsOpen)
        self.assertEqual(0, len(target.Customers))

    def test_Transact_WhenRegisterIsOpenAndHasPeople_CustomerLengthIs0(self) -> None:
        target = Register()
        target.IsOpen = True
        target.Customers.append("Peter")

        target.Transact()

        self.assertEqual(0, len(target.Customers))

    def test_Transact_WhenRegisterIsOpen_CustomerLengthIs0(self) -> None:
        target = Register()
        target.IsOpen = True

        target.Transact()

        self.assertEqual(0, len(target.Customers))

    def test_Transact_WhenRegisterIsClosed_CustomerLengthIs0(self) -> None:
        target = Register()
        target.IsOpen = False

        target.Transact()

        self.assertEqual(0, len(target.Customers))


class ShopTests(unittest.TestCase):
    def test_WhenObjectIsCreated_RegistersLengthIs5(self) -> None:
        target = Shop()

        self.assertEqual(5, len(target.Registers))


unittest.main()
