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

def main() -> None:
    pass

if __name__ == "__main__":
    main()
