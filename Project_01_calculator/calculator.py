from typing import Callable


def add(x: float, y: float) -> float:
    """
    Add two numbers.

    Parameters:
        x (float): The first number.
        y (float): The second number.

    Returns:
        float: The sum of x and y.
    """
    return x + y


def subtract(x: float, y: float) -> float:
    """
    Subtract the second number from the first number.

    Parameters:
        x (float): The first number.
        y (float): The second number.

    Returns:
        float: The difference between x and y.
    """
    return x - y


def multiply(x: float, y: float) -> float:
    """
    Multiply two numbers.

    Parameters:
        x (float): The first number.
        y (float): The second number.

    Returns:
        float: The product of x and y.
    """
    return x * y


def divide(x: float, y: float) -> float:
    """
    Divide the first number by the second number.

    Parameters:
        x (float): The numerator.
        y (float): The denominator.

    Returns:
        float: The result of x divided by y.

    Raises:
        ZeroDivisionError: If y is 0.
    """
    return x / y


def power(x: float, y: float) -> float:
    """
    Raise the first number to the power of the second number.

    Parameters:
        x (float): The base.
        y (float): The exponent.

    Returns:
        float: The result of x raised to the power of y.
    """
    return x ** y  # type: ignore


def modulus(x: float, y: float) -> float:
    """
    Calculate the remainder of the division of the first number by the second number.

    Parameters:
        x (float): The numerator.
        y (float): The denominator.

    Returns:
        float: The remainder of x divided by y.
    """
    return x % y


def get_number(prompt: str) -> float:
    """
    Prompt the user to input a number and handle invalid input.

    Parameters:
        prompt (str): The input prompt to display to the user.

    Returns:
        float: The number entered by the user.
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number like 52 or 3.14")


def main() -> None:
    """
    The main function for the calculator app.
    Allows the user to perform arithmetic operations on two numbers.

    Supported operations:
        + : Addition
        - : Subtraction
        * : Multiplication
        / : Division
        ** : Exponentiation
        % : Modulus
    """
    # Dictionary mapping operation symbols to corresponding functions
    operations: dict[str, Callable[..., float]] = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
        "**": power,
        "%": modulus
    }

    print("Welcome to the calculator app!")
    print("Available operations:", ", ".join(operations.keys()))

    while True:
        # Get the first number
        x: float = get_number("Enter number X: ")

        # Get the operation
        operation_sign: str = input("Enter operation + - / * ** %: ")

        if operation_sign not in operations:
            print(f"Invalid operation '{operation_sign}'. Please choose a valid operation.")
            continue

        # Get the second number
        y: float = get_number("Enter number Y: ")

        # Handle division by zero
        if operation_sign == "/" and y == 0:
            print("Error. You can't divide by 0")
            continue

        # Perform the operation
        operation: Callable[[float, float], float] = operations[operation_sign]
        result: float = operation(x, y)
        print(f"Result: {x} {operation_sign} {y} = {result}")

        # Ask the user if they want to perform another calculation
        another_calculation = input("Do you want to perform another calculation? (y/n): ").strip().lower()
        if another_calculation != "y":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
