import pickle
from typing import Any
from Project_03_habits_tracker_pickle.habit import Habit
from Project_03_habits_tracker_pickle.errors import NotFoundError, AlreadyExistsError


class HabitService:
    """
    Handles habit-related operations for the Habit Tracker application.

    Methods:
        add_habit: Add a new habit to the system.
        complete_habit: Mark a habit as completed.
        remove_habit: Remove an existing habit.
        get_habits: Retrieve the list of all habits.
    """

    def __init__(self) -> None:
        """
        Initializes the HabitService instance, setting up the file name for storing habits and loading existing habits.

        Attributes:
            _repository_file_name (str): The file name used to store habits in pickle format.
            _habits (list[Habit]): The list of all habits currently in the system.
        """
        self._repository_file_name: str = "habits.pickle"
        self._habits: list[Habit] = self.__read_habits()

    def __save_habits(self) -> None:
        """
        Save the current list of habits to the pickle file.
        """
        pickle.dump(self._habits, open(self._repository_file_name, "wb"))

    def __read_habits(self) -> list[Habit] | Any:
        """
        Read habits from the pickle file.

        Returns:
            list[Habit]: The list of habits, or an empty list if no habits are found.
        """
        try:
            return pickle.load(open(self._repository_file_name, "rb"))
        except EOFError:
            return list()

    def get_habits(self) -> list[Habit] | Any:
        """
        Retrieve the list of all habits.

        Returns:
            list[Habit]: The current list of habits.
        """
        return self._habits

    def add_habit(self, new_habit: Habit) -> None:
        """
        Add a new habit to the list, ensuring that it doesn't already exist.

        Parameters:
            new_habit (Habit): The new habit to add.

        Raises:
            AlreadyExistsError: If the habit already exists.
        """
        self.check_if_already_exists(new_habit)
        self._habits.append(new_habit)
        self.__save_habits()

    def complete_habit(self, habit: Habit) -> None:
        """
        Mark a habit as completed.

        Parameters:
            habit (Habit): The habit to complete.

        Raises:
            NotFoundError: If the habit doesn't exist.
        """
        self.check_if_exists(habit)
        habit.complete_habit()
        self.__save_habits()

    def remove_habit(self, habit: Habit) -> None:
        """
        Remove a habit from the list.

        Parameters:
            habit (Habit): The habit to remove.

        Raises:
            NotFoundError: If the habit doesn't exist.
        """
        self.check_if_exists(habit)
        self._habits.remove(habit)
        self.__save_habits()

    def check_if_exists(self, habit: Habit) -> None:
        """
        Check if a habit exists by name.

        Parameters:
            habit (Habit): The habit to check.

        Raises:
            NotFoundError: If the habit doesn't exist.
        """
        if not self.is_existing_habit_by_name(habit.name):
            raise NotFoundError(f"The habit '{habit.name}' doesn't exist, please add it first.")

    def check_if_already_exists(self, habit: Habit) -> None:
        """
        Check if a habit already exists by name.

        Parameters:
            habit (Habit): The habit to check.

        Raises:
            AlreadyExistsError: If the habit already exists.
        """
        if self.is_existing_habit_by_name(habit.name):
            raise AlreadyExistsError(f"Can't add {habit.name}, because the habit already exists.")

    def is_existing_habit_by_name(self, habit_name: str) -> bool:
        """
        Check if a habit with the specified name exists.

        Parameters:
            habit_name (str): The name of the habit to check.

        Returns:
            bool: True if the habit exists, False otherwise.
        """
        return self.get_habit_index_by_name(habit_name) > -1

    def get_habit_index_by_name(self, habit_name: str) -> int:
        """
        Get the index of a habit by name.

        Parameters:
            habit_name (str): The name of the habit.

        Returns:
            int: The index of the habit if found, -1 if not found.
        """
        habit_index: int = -1
        for index, habit in enumerate(self._habits):
            if habit.name == habit_name:
                habit_index = index
                break

        return habit_index
