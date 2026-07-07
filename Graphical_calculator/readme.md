# Graphical Calculator

Graphical Calculator is my first year project in high school. It's a simple GUI app that can calculate the least common multiple (LCM) and greatest common divisor (GCD) of 2 or 3 integers and the Prime Number Product of an integer.

## Current Features
  * GUI
  * GCD for 2 or 3 integers
  * LCM for 2 or 3 integers
  * Prime Number Product of an integer
  * Custom `MyMath` class
  * Custom exceptions for invalid operations

## GUI Menu Explanation
  * On the right hand side choose an operation.
  * On the left enter 2 or 3 integers if LCM or GCD was chosen and only 1 integer if Prime Number Product was chosen.
  * Press Enter to get the result, the result will appear in green under the integer entry field.
  * Errors will appear in red under the integer entry field with explanation.
  * Press Delete to delete the result text.
  * Press the Quit button to exit from the application.

## How LCM Works
  1. Multiply the 2 numbers.
	2. Divide the result by the GCD of the 2 numbers.

## How GCD works
  1. Assign the second number to the first number.
  2. Assign the remainder of the division between the first number with the second number to the second number.
  3. Repeat until the second number is 0 (Euclid's Algorithm).
  4. If the result is 1, it means that the two numbers are co-prime, meaning they don't have a common divisor except number 1.

## How Prime Number Product works
  1. Start with the entered number.
  2. Find the smallest divisor starting from `2`.
  3. Add that divisor to the product list.
  4. Divide the number by that divisor.
  5. Repeat until the number is reduced to `1`.

## How to Run
Change the working directory to the project folder:
```bash
cd "Graphical Calculator"
```

Run the program:
```bash
python graphical_calculator.py
```

On Windows, this also works:
```bash
python .\graphical_calculator.py
```

## Design Notes
  * The application uses tkinter for the graphical user interface.
  * The main window is represented by the App class, which inherits from tk.Tk.
  * User input is entered as text and then validated before any calculation is performed.
  * For LCM and GCD, the user enters 2 or 3 integers separated by semicolons.
  * For prime number product, only one integer is accepted.
  * The MyMath class contains shared mathematical helper methods used by the Gcd and Lcm classes.
  * The Gcd class uses Euclid's algorithm to calculate the greatest common divisor.
  * The Lcm class calculates the least common multiple using the GCD result.
  * Prime number product is handled by a separate PrimeNumberProduct class.
  * Invalid input is handled with custom exceptions and displayed to the user in red.
  * Successful results are displayed in green.

## Status
Completed. This project passed with the highest mark.
