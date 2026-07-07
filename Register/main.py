from exceptions import (
    AllRegistersClosedException, 
    RegisterAlreadyOpenException, 
    RegisterAlreadyClosedException, 
    CannotCloseLastRegisterWithCustomersException, 
    InvalidRegisterNumberException, 
    RegisterIsClosedException, 
    NoCustomersInRegisterException
) 
from shop import Shop

CUSTOM_EXCEPTIONS = (
    AllRegistersClosedException,
    RegisterAlreadyOpenException,
    RegisterAlreadyClosedException,
    CannotCloseLastRegisterWithCustomersException,
    InvalidRegisterNumberException,
    RegisterIsClosedException,
    NoCustomersInRegisterException
)

def print_menu() -> None:
    print()
    print("=== Shop Simulation ===")
    print("1 - Show registers")
    print("2 - Add customer")
    print("3 - Serve customer")
    print("4 - Open register")
    print("5 - Close register")
    print("6 - Balance customers")
    print("0 - Exit")
    print()

def print_registers(shop: Shop) -> None:
    print()
    print(f"Registers open: {shop.OpenRegisterCount} | Total registers: {len(shop.Registers)}")

    for idx, register in enumerate(shop.Registers):
        display_number = idx + 1

        if register.IsOpen:
            status = "Open"
        else:
            status = "Closed"

        customers = ", ".join(register.Customers)

        if customers == "":
            customers = "No customers"

        print(f"Register {display_number}: {status:<6} | {customers}")

    print()

def read_register_index(shop: Shop) -> int:
    user_input = input(f"Register number (1 - {len(shop.Registers)}): ")

    register_number = int(user_input)

    return register_number - 1

def add_customer_ui(shop: Shop) -> None:
    name = input("Customer name: ".strip())

    if name == "":
        print("Customer name can't be empty")
        return

    shop.AddNewCustomer(name)

    print(f"Customer {name} successfully added")

def serve_customer_ui(shop: Shop) -> None:
    register_index = read_register_index(shop)

    shop.ServeCustomer(register_index)

    print("Customer served")

def main() -> None:
    pass

if __name__ == "__main__":
    main()
