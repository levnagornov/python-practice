from Project_04_quiz.quiz_task import QuizTask


class QuizView:
    """
    A class that handles displaying content to the user in the quiz application.

    The `QuizView` class is responsible for presenting quiz questions,
    options, results, and messages to the user. It ensures that the user
    receives appropriate feedback during the quiz process.
    """

    def show_quiz_task(self, task: QuizTask) -> None:
        """
        Displays a quiz question with its corresponding options to the user.

        Args:
            task (QuizTask): The task to be displayed, which includes a
                             question, options, and the correct answer.
        """
        print(task.question)
        for i, option in enumerate(task.options, 1):
            print(f"  {i}. {option}")

    def show_message(self, message: str) -> None:
        """
        Displays a generic message to the user.

        Args:
            message (str): The message to be displayed.
        """
        print(message)

    def show_welcome_message(self) -> None:
        """
        Displays a welcome message to the user at the start of the quiz.
        """
        print("### Welcome to my simple quiz! ###")

    def show_results(self, correct_answers: int, total_questions: int) -> None:
        """
        Displays the results of the quiz after all questions have been answered.

        Args:
            correct_answers (int): The number of correct answers the user provided.
            total_questions (int): The total number of questions in the quiz.
        """
        print(f"Results: you answered {correct_answers} out of {total_questions} questions correctly.")
