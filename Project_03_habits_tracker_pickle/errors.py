class NotFoundError(Exception):
    """
    Raised when the specified element (habit) is not found.

    Attributes:
        message (str): The error message that will be displayed when the exception is raised.

    Methods:
        __init__: Initializes the exception with a custom error message.
        __str__: Returns the error message as a string for display.
    """

    def __init__(self, message: str = "The element is not found.") -> None:
        self.message = f"Error. {message}"
        super().__init__(self.message)

    def __str__(self) -> str:
        return self.message


class AlreadyExistsError(Exception):
    """
    Raised when the specified element (habit) already exists.

    Attributes:
        message (str): The error message that will be displayed when the exception is raised.

    Methods:
        __init__: Initializes the exception with a custom error message.
        __str__: Returns the error message as a string for display.
    """

    def __init__(self, message: str = "The element already exists.") -> None:
        self.message = f"Error. {message}"
        super().__init__(self.message)

    def __str__(self) -> str:
        return self.message
