from Project_04_quiz.quiz_controller import QuizController
from Project_04_quiz.quiz_service import QuizService
from Project_04_quiz.quiz_view import QuizView
from Project_04_quiz.input_manager import InputManger


def main() -> None:
    """
    The main entry point for the quiz application.

    Initializes the necessary components of the quiz application and
    starts the quiz process. This function creates instances of the
    `QuizService`, `QuizView`, `InputManger`, and `QuizController` classes,
    and then runs the quiz using the `QuizController`.

    The flow of the application is as follows:
    1. `QuizService` handles fetching the quiz tasks and replies.
    2. `QuizView` manages displaying information to the user.
    3. `InputManger` handles user input.
    4. `QuizController` manages the flow of the quiz by interacting with the above components.

    The quiz consists of a set of tasks, where users must select the correct answer
    from a list of options. The user is provided feedback on their performance after each question
    and at the end of the quiz.
    """
    # Initialize the necessary components
    quiz_service: QuizService = QuizService()
    quiz_view: QuizView = QuizView()
    input_manger: InputManger = InputManger()
    quiz_controller: QuizController = QuizController(quiz_service, quiz_view, input_manger)

    # Run the quiz
    quiz_controller.run()


if __name__ == '__main__':
    main()
