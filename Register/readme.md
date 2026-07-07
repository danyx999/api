# Register

## Description

Register is a command-line shop register simulation written in Python.
The project simulates multiple shop registers, customer queues, opening and closing registers, serving customers, redistribution and queue balancing.

## Current Features

* Command-line interface
* Five shop registers
* Open and closed register states
* Adding customers to the register with the fewest customers
* Serving customers from a selected register
* Opening and closing registers
* Redistributing customers when a register is closed
* Balancing customers across open registers
* Custom exceptions for invalid operations
* Unit tests using Python's `unittest` module

## CLI Menu Explanation

The user can choose from these options:

### 1 - Show registers

Displays:

* Number of open registers
* Total number of registers
* Status of each register: open or closed
* Customer names in each queue

### 2 - Add customer

* The user enters the name of the new customer.
* Whitespace is removed from the beginning and end of the name.
* Empty names are rejected.
* The customer is added to the open register with the fewest customers.
* A success message is displayed.

### 3 - Serve customer

* The user enters the register number.
* The first customer in that register's queue is served.
* A success message is displayed.

### 4 - Open register

* The user enters which register to open.
* The selected register is opened.
* Customers are balanced across open registers.
* A success message is displayed.

### 5 - Close register

* The user enters which register to close.
* Customers from the selected register are redistributed across the remaining open registers.
* The selected register is closed.
* A success message is displayed.

### 6 - Balance customers

* Customers are balanced across all open registers.
* A success message is displayed.

### 0 - Exit

* Exits the simulation.

After each operation, the user is asked to press Enter to continue.

## How Register Numbering Works

* Registers are displayed to the user using numbers from `1` to `5`.
* Internally, registers are stored using zero-based indices from `0` to `4`.
* User input is converted before calling the internal logic.

## How Redistribution Works

When a register is closed:

1. Customers from the selected register are stored.
2. The selected register is closed.
3. The stored customers are passed into the redistribution function.
4. The customer list is reversed.
5. Customers are added one by one to the open register with the fewest customers.

Customers from the back of the queue are redistributed first.

## How Rebalancing Works

When customers are balanced:

1. The open register with the most customers is found.
2. The last customer from that register's queue is removed.
3. The open register with the fewest customers is found.
4. The customer is moved there.
5. This repeats until the difference between the largest and smallest open queue is `0` or `1`.

## How to Run

Change the working directory to the project folder:

```bash
cd Register
```

Run the program:

```bash
python main.py
```

On Windows, this also works:

```bash
python .\main.py
```

## How to Run Tests

Change the working directory to the project folder:

```bash
cd Register
```

Run all tests:

```bash
python -m unittest
```

Or run the test file directly:

```bash
python test_register_shop.py
```

On Windows, this also works:

```bash
python .\test_register_shop.py
```

## Design Notes

* The `Shop` class contains the main business logic.
* The CLI only handles input, output and calling `Shop` methods.
* Registers are displayed to the user starting from `1`.
* Internally, registers use zero-based indexing.
* Customer queues are represented using lists.
* When customers are redistributed or balanced, customers from the back of the queue are moved first.
* Invalid operations are handled using custom exceptions.

## Known Limitations

* Customers are only represented only as names.
* There is no save/load system.
* Products, prizes and serving times are not implemented.

## Possible Future Improvements

* Dedicated `Customer` class
* Products and prices
* Serving time based on product count
* Session statistics
* Save/load system
* Proximity-based redistribution and balancing

## Status

Completed v1.0. Further improvements may be added later.
