# Habit Tracker
A Python-based command-line application for tracking and managing personal habits. This app allows users to create, complete, view, and remove habits while tracking their progress.

## Features
- **Manage Habits**:
  - Add new habits to the tracker.
  - Mark habits as completed, and track streaks.
  - Remove habits from the tracker.
- **Progress Tracking**:
  - View the progress of habits, including streaks and the last completion date.
  - Get feedback on habits' status (e.g., "not started yet", "done X times").
- **Error Handling**:
  - Handles scenarios like attempting to add a duplicate habit or complete a non-existing habit.

## Usage
1. Run the script:
   ```bash
   python main.py
2. Use the menu options to:
   - Add a new habit.
   - Mark a habit as completed.
   - View habit progress.
   - Remove a habit.  

3. The application will guide you through the process and display the results.
   
## Example Interaction
```text
### Habit Tracker menu: ###
  1. Add habit
  2. Mark completed
  3. Show progress
  4. Remove habit
  0. Exit
Enter the option number: 1
Enter the name of the habit: Drink water
The habit 'Drink water' has been successfully added!

### Habit Tracker menu: ###
  1. Add habit
  2. Mark completed
  3. Show progress
  4. Remove habit
  0. Exit
Enter the option number: 2
Choose a habit to complete it:
  1. Drink water: done 0 times, not started yet.
Enter the habit number to complete: 1
The habit 'Drink water' has been successfully completed!
```

## Requirements

Python 3.12 or higher.

## Extending the Application

To add new features:
- Update the `Habit` class to include additional tracking data (e.g., duration, notes).  
- Modify the `HabitService` and `HabitView` classes to support the new data.
- Extend the menu options in `HabitController` to provide new functionality.

## License
MIT  
This project is open-source and provided as-is. You are free to use, modify, and share it.

Author: Lev Nagornov  
Date: 01-01-2025