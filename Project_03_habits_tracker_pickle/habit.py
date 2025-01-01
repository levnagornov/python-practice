from dataclasses import dataclass
from datetime import datetime


@dataclass
class Habit:
    """
    Represents a habit in the Habit Tracker application.

    Attributes:
        name (str): The name of the habit.
        last_completed (datetime): The timestamp of the last time the habit was completed.
        streak (int): The number of times the habit has been completed consecutively.

    Methods:
        complete_habit: Mark the habit as completed and update the streak and last completed time.
    """

    name: str
    last_completed: datetime = datetime.now()
    streak: int = 0

    def complete_habit(self) -> None:
        """
        Mark the habit as completed, increase the streak, and update the last completed time.

        The streak is incremented by 1, and the `last_completed` timestamp is updated to the current time.
        """
        self.streak += 1
        self.last_completed = datetime.now()
