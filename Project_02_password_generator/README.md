# Password Generator
A Python-based command-line application for generating secure passwords based on user-defined preferences.

## Features
- **Customizable Passwords**:
  - Specify the desired password length.
  - Choose whether to include uppercase letters, numbers, and special characters.
- **Security**:
  - Ensures at least one character from each selected category is included.
  - Randomizes character order for improved security.
- **User-Friendly**:
  - Prompts guide the user through the password generation process.
  - Handles invalid input gracefully.

## Usage
1. Run the script:
   ```bash
   python password_generator.py
   ```
2. Follow the prompts to specify:
   - Length of the password.
   - Whether to include uppercase letters.
   - Whether to include numbers.
   - Whether to include special characters.
3. View the generated password.

## Example Interaction
```text
Enter the length of the password: 12
Should we include uppercase letters? y/n: y
Should we include numbers? y/n: y
Should we include special characters? y/n: n
Generated password:
 a7BcdefG3HjL
```

## Requirements
Python 3.12 or higher.

## Extending the Application
To add new character categories or features:
1. Modify the `generate_password` function to include the new logic.
2. Update the prompts and parameters in the `main()` function.

## License

This project is open-source and provided as-is. You are free to use, modify, and share it.

Author: Lev Nagornov  
Date: 30-12-2024