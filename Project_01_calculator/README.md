# Calculator App
This is a simple command-line calculator application built with Python. 
It allows users to perform basic arithmetic operations on two numbers.

## Features
- Supports the following operations:
  - `+` : Addition
  - `-` : Subtraction
  - `*` : Multiplication
  - `/` : Division
  - `**` : Exponentiation
  - `%` : Modulus
- Input validation to ensure users enter valid numbers.
- Handles division by zero gracefully.
- User-friendly design with prompts and error messages.
- Extensible architecture for adding more operations.

## Usage
1. Run the script in a Python environment:
    ```bash
    python calculator.py
    ```
2. Enter the first number when prompted.
3. Choose an operation by typing one of the supported symbols (+, -, *, /, **, %).
4. Enter the second number.
5. View the result of the calculation.
6. You can perform additional calculations or exit the program.

## Example Interaction
```text
Welcome to the calculator app!
Available operations: +, -, *, /, **, %

Enter number X: 5
Enter operation + - / * ** %: *
Enter number Y: 3
Result: 5 * 3 = 15

Do you want to perform another calculation? (y/n): n
Goodbye!
```

## Requirements
- Python 3.12 or higher.

## Extending the Application
To add a new operation:
1. Define a new function in the codebase.
2. Add the operation to the operations dictionary in the `main()` function.

Example:
```python
operations = {
        ...,
        # add here a new symbol and a function
    }

def new_operation(x: float, y: float) -> float:
    return x # Some logic here

operations["new_symbol"] = new_operation  
```

## License
MIT  
This project is open-source and provided as-is. Feel free to use, modify, and share it.

Author: Lev Nagornov  
Date: 29-12-2024
