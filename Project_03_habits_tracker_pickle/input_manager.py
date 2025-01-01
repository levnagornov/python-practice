import sys


class InputManger:
    """
    Handles user input for the Habit Tracker application.

    Methods:
        get_user_str_input: Get a sanitized string input from the user.
        get_user_int_input: Get an integer input within a specified range.
    """

    @staticmethod
    def get_user_str_input(prompt: str) -> str:
        """
        Get a string input from the user and strip extra whitespace.

        Parameters:
            prompt (str): The message displayed to the user.

        Returns:
            str: The sanitized string input from the user.
        """
        return input(prompt).strip()

    def get_user_int_input(
        self,
        min_value: int = -sys.maxsize - 1,
        max_value: int = sys.maxsize,
        prompt: str = "Enter the option number: "
    ) -> int:
        """
        Get an integer input from the user within a specified range.

        Parameters:
            min_value (int): The minimum allowable value (default is -sys.maxsize - 1).
            max_value (int): The maximum allowable value (default is sys.maxsize).
            prompt (str): The message displayed to the user (default is "Enter the option number: ").

        Returns:
            int: The validated integer input from the user.

        Raises:
            ValueError: If the user input is not a valid integer or is out of the specified range.
        """
        while True:
            try:
                value = int(self.get_user_str_input(prompt))
                if min_value <= value <= max_value:
                    return value

                print("Invalid option.")
            except ValueError:
                print("Invalid input. Please enter a number.")