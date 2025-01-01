from Project_03_habits_tracker_pickle.menu_item import MenuItem
from Project_03_habits_tracker_pickle.habit import Habit
from Project_03_habits_tracker_pickle.habit_service import HabitService
from Project_03_habits_tracker_pickle.habit_view import HabitView
from Project_03_habits_tracker_pickle.input_manager import InputManger
from Project_03_habits_tracker_pickle.errors import NotFoundError, AlreadyExistsError


class HabitController:
    """
    The central controller for the Habit Tracker application.

    Attributes:
        _habit_service (HabitService): Manages habit-related operations.
        _habit_view (HabitView): Handles display of messages and menus to the user.
        _input_manager (InputManager): Manages user input.
    """

    def __init__(self, hs: HabitService, hv: HabitView, im: InputManger):
        """
        Initialize the controller with the required service, view, and input manager.

        Parameters:
            hs (HabitService): The habit service instance.
            hv (HabitView): The habit view instance.
            im (InputManager): The input manager instance.
        """
        self._habit_service: HabitService = hs
        self._habit_view: HabitView = hv
        self._input_manager: InputManger = im

    def get_menu_items(self) -> list[MenuItem]:
        """
        Define the list of menu items for the user interface.

        Returns:
            list[MenuItem]: A list of menu options with corresponding actions.
        """
        return [
            MenuItem(1, "Add habit", self.run_add_habit_menu),
            MenuItem(2, "Mark completed", self.run_mark_completed_menu),
            MenuItem(3, "Show progress", self.run_show_progress_menu),
            MenuItem(4, "Remove habit", self.run_remove_habit_menu),
            MenuItem(0, "Exit", self.run_exit_menu),
        ]

    def run_add_habit_menu(self) -> None:
        """Handle the 'Add habit' menu option."""
        self._habit_view.show_message("### Add a new habit: ###")
        habit_name: str = self._input_manager.get_user_str_input("Enter the name of the habit: ")
        habit: Habit = Habit(habit_name)
        try:
            self._habit_service.add_habit(habit)
            self._habit_view.show_message(f"The habit '{habit_name}' has been successfully added!")
        except AlreadyExistsError as error:
            self._habit_view.show_message(error.message)

    def run_mark_completed_menu(self) -> None:
        """Handle the 'Mark completed' menu option."""
        habits: list[Habit] = self._habit_service.get_habits()
        if not habits:
            self._habit_view.show_message("### There are no habits yet, please create one first! ###")
            return

        self._habit_view.show_message("### Choose a habit to complete it: ###")
        self._habit_view.show_habits(habits)
        try:
            choice: int = self._input_manager.get_user_int_input(1, len(habits))
            habit: Habit = habits[choice - 1]
            self._habit_service.complete_habit(habit)
            self._habit_view.show_message(f"The habit '{habit.name}' has been successfully completed!\n")
        except IndexError:
            self._habit_view.show_message("There is no such option.")
        except NotFoundError as error:
            self._habit_view.show_message(error.message)

    def run_show_progress_menu(self) -> None:
        """Handle the 'Show progress' menu option."""
        habits: list[Habit] = self._habit_service.get_habits()
        if not habits:
            self._habit_view.show_message("### There are no habits yet, please create one first! ###")
            return

        self._habit_view.show_habits(habits)

    def run_remove_habit_menu(self) -> None:
        """Handle the 'Remove habit' menu option."""
        habits: list[Habit] = self._habit_service.get_habits()
        if not habits:
            self._habit_view.show_message("### There are no habits yet, please create one first! ###")
            return

        self._habit_view.show_message("### Choose a habit for removal: ###")
        self._habit_view.show_habits(habits)
        try:
            choice: int = self._input_manager.get_user_int_input(1, len(habits))
            habit: Habit = habits[choice - 1]
            self._habit_service.remove_habit(habit)
            self._habit_view.show_message(f"The habit '{habit.name}' has been successfully removed!\n")
        except NotFoundError as error:
            self._habit_view.show_message(error.message)

    @staticmethod
    def run_exit_menu() -> None:
        """Handle the 'Exit' menu option."""
        print("Goodbye!")
        exit(0)

    def run(self) -> None:
        """
        Main application loop. Displays the menu, handles user input, and runs the selected action.
        """
        while True:
            menu_items: list[MenuItem] = self.get_menu_items()
            self._habit_view.show_menu(menu_items)
            selected_item_position: int = self._input_manager.get_user_int_input(0, len(menu_items))
            menu_item: MenuItem = next((item for item in menu_items if item.position == selected_item_position))
            menu_item.action()
