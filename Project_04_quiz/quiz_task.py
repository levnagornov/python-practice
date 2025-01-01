class QuizTask:
    """
    A class representing a quiz question, its options, and the correct answer.

    The `QuizTask` class holds the question for the quiz, a list of possible
    answer options, and the correct answer. It provides a method to check
    if a given answer is correct.
    """

    def __init__(self, question: str, options: list[str], correct_answer: str) -> None:
        """
        Initializes a QuizTask with a question, options, and a correct answer.

        Args:
            question (str): The quiz question.
            options (list[str]): A list of possible answers to the question.
            correct_answer (str): The correct answer from the options.
        """
        self.question: str = question
        self.options: list[str] = options
        self.correct_answer: str = correct_answer

    def is_correct_answer(self, answer: str) -> bool:
        """
        Checks if the provided answer matches the correct answer.

        Args:
            answer (str): The answer to check.

        Returns:
            bool: True if the provided answer is correct, False otherwise.
        """
        return self.correct_answer == answer
