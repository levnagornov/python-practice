from Project_04_quiz.quiz_service import QuizService
from Project_04_quiz.quiz_view import QuizView
from Project_04_quiz.quiz_task import QuizTask
from Project_04_quiz.input_manager import InputManger


class QuizController:
    """
    Controller class for managing the quiz flow, handling quiz tasks, and displaying results.

    The `QuizController` class is responsible for controlling the quiz game. It interacts with
    the `QuizService` to fetch quiz tasks, the `QuizView` to display messages and results to
    the user, and the `InputManager` to get user inputs during the game.
    """

    def __init__(self,
                 quiz_service: QuizService,
                 quiz_view: QuizView,
                 input_manger: InputManger) -> None:
        """
        Initializes the QuizController with the given services and initializes the correct answers counter.

        Args:
            quiz_service (QuizService): The service to handle quiz logic and fetch tasks.
            quiz_view (QuizView): The view to display messages and task prompts to the user.
            input_manger (InputManger): The input manager to handle and validate user input.
        """
        self.__quiz_service: QuizService = quiz_service
        self.__quiz_view: QuizView = quiz_view
        self.__input_manger: InputManger = input_manger
        self.__correct_answers_counter: int = 0

    def run(self) -> None:
        """
        Starts the quiz game by showing the welcome message, fetching random quiz tasks,
        and iterating through them for user interaction.

        After completing all tasks, it displays the results of the quiz.
        """
        self.__quiz_view.show_welcome_message()
        quiz_tasks: list[QuizTask] = self.__quiz_service.get_random_tasks()
        for i, task in enumerate(quiz_tasks, 1):
            self.play_task(task)

        self.__quiz_view.show_results(self.__correct_answers_counter, len(quiz_tasks))

    def play_task(self, task: QuizTask) -> None:
        """
        Displays a quiz task to the user, accepts the user's answer, checks if it's correct,
        and provides feedback based on the user's response.

        Args:
            task (QuizTask): The quiz task that contains the question and options.
        """
        self.__quiz_view.show_quiz_task(task)
        choice: int = self.__input_manger.get_user_int_input(1, len(task.options))
        answer: str = task.options[choice - 1]
        if task.is_correct_answer(answer):
            right_reply: str = self.__quiz_service.get_random_right_reply()
            self.__quiz_view.show_message(right_reply)
            self.__correct_answers_counter += 1
        else:
            wrong_reply: str = self.__quiz_service.get_random_wrong_reply()
            self.__quiz_view.show_message(wrong_reply)
            self.__quiz_view.show_message(f"The correct answer is {task.correct_answer}")
        print()
