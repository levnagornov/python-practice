# Quiz Game
A Python-based command-line application for playing a quiz. This app allows users to answer random quiz questions and see their results at the end.

## Features
- **Quiz Gameplay**:
  - Get random quiz tasks with multiple answer options.
  - Choose answers and get immediate feedback on correctness.
  - Track the number of correct answers during the quiz session.
- **User Interaction**:
  - The application guides the user through the questions with interactive prompts.
  - Displays a welcome message and results at the end of the quiz.
- **Randomized Responses**:
  - Provides random feedback for correct and incorrect answers.
  - Randomizes the quiz questions and answer options for variety.

## Usage
1. Run the script:
   ```bash
   python main.py
2. The application will:
   - Display a welcome message and start the quiz.
   - Ask questions and show answer options.
   - Allow you to select your answer by entering the number of the option.
3. After answering all questions, the application will display your results, showing how many questions you answered correctly.

## Example Interaction
```text
### Welcome to my simple quiz! ###
Question 1: What is the capital of France?
  1. Berlin
  2. Paris
  3. Madrid
Enter the option number: 2
Correct! Well done!

Question 2: What is 2 + 2?
  1. 3
  2. 4
  3. 5
Enter the option number: 2
Correct! Well done!

Results: you answered 2 out of 2 questions correctly.
```

## Requirements
Python 3.12 or higher.

## Extending the Application
Add more quiz questions:
- Modify the `quiz_tasks.json` file with additional quiz questions.
- Add new question categories if desired.  

Add different types of questions:
- Modify the `QuizTask` class to support other question formats, such as true/false.

Modify user feedback:
- Customize the responses for correct and incorrect answers by modifying the `replies.json` file.

## License
MIT  
This project is open-source and provided as-is. You are free to use, modify, and share it.

Author: Lev Nagornov
Date: 01-01-2025