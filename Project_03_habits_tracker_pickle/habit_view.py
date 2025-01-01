from Project_03_habits_tracker_pickle.habit import Habit
from Project_03_habits_tracker_pickle.menu_item import MenuItem


class HabitView:
    """
    Handles the user interface for the Habit Tracker application.

    Methods:
        show_menu: Display the main menu with available actions.
        show_message: Show a custom message to the user.
        show_habits: Display a list of habits with details about their progress.
    """

    @staticmethod
    def show_menu(menu_items: list[MenuItem]) -> None:
        """
        Display the main menu with available actions.

        Parameters:
            menu_items (list[MenuItem]): The list of menu items to display.
        """
        print("### Habit Tracker Menu: ###")
        for item in menu_items:
            print(f"  {item.position}. {item.title}")

    @staticmethod
    def show_message(message: str) -> None:
        """
        Display a custom message to the user.

        Parameters:
            message (str): The message to display.
        """
        print(message)

    @staticmethod
    def show_habits(habits: list[Habit]) -> None:
        """
        Display a list of habits with details about their progress.

        Parameters:
            habits (list[Habit]): The list of habits to display.
        """
        habits_number: int = len(habits)
        if habits_number == 1:
            HabitView.show_message(f"There is only {habits_number} habit in total.")
        else:
            HabitView.show_message(f"There are {habits_number} habits in total.")

        for i, habit in enumerate(habits, 1):
            streak_message = f"done {habit.streak} time{'s' if habit.streak > 1 or habit.streak == 0 else ''}"
            last_completed = (
                f"last completed on {habit.last_completed.strftime('%Y-%m-%d %H:%M')}"
                if habit.streak > 0 else "not started yet"
            )
            print(f"  {i}. {habit.name}: {streak_message}, {last_completed}.")
        print()