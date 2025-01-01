import sys


class InputManger:
    """
    A class that provides methods for handling user input.

    The `InputManger` class provides functionality to safely handle user input
    from the console. It includes methods for receiving string and integer inputs
    from the user while ensuring that the input is validated and within a specified range.
    """

    @staticmethod
    def get_user_str_input(prompt: str) -> str:
        """
        Prompts the user for a string input and returns the input with leading/trailing spaces removed.

        Args:
            prompt (str): The message to be displayed to the user before receiving input.

        Returns:
            str: The input string provided by the user, stripped of leading and trailing whitespace.
        """
        return input(prompt).strip()

    def get_user_int_input(
            self,
            min_value: int = -sys.maxsize - 1,
            max_value: int = sys.maxsize,
            prompt: str = "Enter the option number: "
    ) -> int:
        """
        Prompts the user for an integer input and validates that the input is within the specified range.

        This method continues prompting the user for input until a valid integer within the given range is provided.

        Args:
            min_value (int, optional): The minimum valid value for the input. Defaults to the lowest possible integer.
            max_value (int, optional): The maximum valid value for the input. Defaults to the highest possible integer.
            prompt (str, optional): The message to display to the user when requesting input. Defaults to 'Enter the option number: '

        Returns:
            int: The valid integer input provided by the user.

        Raises:
            ValueError: If the user inputs a non-integer or a value outside the specified range.
        """
        while True:
            try:
                value = int(self.get_user_str_input(prompt))
                if min_value <= value <= max_value:
                    return value
                print(f"Invalid option. Please enter a number between {min_value} and {max_value}.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
