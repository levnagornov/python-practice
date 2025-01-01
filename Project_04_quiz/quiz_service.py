import json
import random

from Project_04_quiz.quiz_task import QuizTask


class QuizService:
    """
    Service class that manages quiz tasks and handles responses.

    The `QuizService` class is responsible for loading quiz tasks from a JSON file,
    providing random tasks to the user, and fetching random replies for correct and
    incorrect answers. It interacts with `QuizTask` objects and uses JSON data for task
    and reply content.
    """

    def __init__(self) -> None:
        """
        Initializes the QuizService by reading quiz tasks and replies from JSON files.

        This constructor loads tasks, correct answer replies, and incorrect answer replies
        into memory by calling respective helper methods that read from external JSON files.
        """
        self.tasks: list[QuizTask] = self.__read_tasks()
        self.__right_answer_replies: list[str] = self.__read_right_replies()
        self.__wrong_answer_replies: list[str] = self.__read_wrong_replies()

    def __read_tasks(self) -> list[QuizTask]:
        """
        Reads and loads quiz tasks from the 'quiz_tasks.json' file.

        This private method parses the JSON data from the 'quiz_tasks.json' file
        and creates `QuizTask` objects for each task.

        Returns:
            list[QuizTask]: A list of `QuizTask` objects loaded from the JSON file.
        """
        with open("quiz_tasks.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        tasks: list[QuizTask] = [
            QuizTask(
                question=item["question"],
                options=item["options"],
                correct_answer=item["correct_answer"]
            )
            for item in data
        ]
        return tasks

    def __read_right_replies(self) -> list[str]:
        """
        Reads and loads correct answer replies from the 'replies.json' file.

        This private method parses the JSON data from the 'replies.json' file
        and extracts the list of correct answer replies.

        Returns:
            list[str]: A list of strings representing replies for correct answers.
        """
        with open("replies.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        right_replies: list[str] = data["right_answer_replies"]
        return right_replies

    def __read_wrong_replies(self) -> list[str]:
        """
        Reads and loads incorrect answer replies from the 'replies.json' file.

        This private method parses the JSON data from the 'replies.json' file
        and extracts the list of incorrect answer replies.

        Returns:
            list[str]: A list of strings representing replies for incorrect answers.
        """
        with open("replies.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        wrong_replies: list[str] = data["wrong_answer_replies"]
        return wrong_replies

    def get_random_tasks(self, amount: int = 10) -> list[QuizTask]:
        """
        Returns a random selection of quiz tasks.

        This method selects a random subset of quiz tasks from the full list
        of tasks, with a default of 10 tasks.

        Args:
            amount (int, optional): The number of tasks to select. Defaults to 10.

        Returns:
            list[QuizTask]: A list of randomly selected `QuizTask` objects.
        """
        return random.sample(self.tasks, amount)

    def get_random_right_reply(self) -> str:
        """
        Returns a random reply for a correct answer.

        This method selects a random string from the list of correct answer replies.

        Returns:
            str: A random reply for a correct answer.
        """
        return random.choice(self.__right_answer_replies)

    def get_random_wrong_reply(self) -> str:
        """
        Returns a random reply for an incorrect answer.

        This method selects a random string from the list of incorrect answer replies.

        Returns:
            str: A random reply for an incorrect answer.
        """
        return random.choice(self.__wrong_answer_replies)
