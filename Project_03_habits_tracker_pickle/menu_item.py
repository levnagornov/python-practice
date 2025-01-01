from typing import Callable


class MenuItem:
    """
    Represents a single menu item in the Habit Tracker application.

    Attributes:
        position (int): The position of the menu item in the menu list.
        title (str): The title of the menu item for display purposes.
        action (Callable[..., None]): The action (function) to execute when the menu item is selected.
    """

    def __init__(self, position: int, title: str, action: Callable[..., None]):
        """
        Initialize a new MenuItem instance.

        Parameters:
            position (int): The position of the menu item in the menu.
            title (str): The display name of the menu item.
            action (Callable[..., None]): The function to execute when the menu item is selected.
        """
        self.position: int = position
        self.title: str = title
        self.action: Callable[..., None] = action
