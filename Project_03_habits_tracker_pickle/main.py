from Project_03_habits_tracker_pickle.habit_service import HabitService
from Project_03_habits_tracker_pickle.habit_view import HabitView
from Project_03_habits_tracker_pickle.input_manager import InputManger
from Project_03_habits_tracker_pickle.habit_controller import HabitController


def main() -> None:
    """
    Initialize and run the Habit Tracker application.

    Components:
        - HabitService: Manages habit-related data and logic.
        - HabitView: Provides the user interface for displaying habit data.
        - InputManger: Handles user input.
        - HabitController: Connects the service, view, and input manager to handle application flow.
    """
    # Initialize core components
    habit_service: HabitService = HabitService()
    habit_view: HabitView = HabitView()
    input_manger: InputManger = InputManger()
    habit_controller: HabitController = HabitController(habit_service, habit_view, input_manger)

    # Run the application
    habit_controller.run()


if __name__ == '__main__':
    main()
