import random
import string


def generate_password(
        password_length: int,
        is_uppercase_included: bool = True,
        is_numbers_included: bool = True,
        is_special_characters_included: bool = True
) -> str:
    """
    Generate a secure password based on specified criteria.

    Parameters:
        password_length (int): Length of the password to be generated.
        is_uppercase_included (bool): Whether to include uppercase letters in the password.
        is_numbers_included (bool): Whether to include numbers in the password.
        is_special_characters_included (bool): Whether to include special characters in the password.

    Returns:
        str: The generated password.
    """
    # Define character sets based on user preferences
    letters: str = string.ascii_letters if is_uppercase_included else string.ascii_lowercase
    numbers: str = string.digits if is_numbers_included else ""
    punctuation_marks: str = string.punctuation if is_special_characters_included else ""
    all_characters: str = letters + numbers + punctuation_marks
    password: list[str] = []

    # Ensure the inclusion of at least one character from each selected category
    if letters:
        password.append(random.choice(letters))
    if numbers:
        password.append(random.choice(numbers))
    if punctuation_marks:
        password.append(random.choice(punctuation_marks))

    # Fill the remaining characters randomly
    password += [
        random.choice(all_characters)
        for _ in range(password_length - len(password))
    ]

    # Shuffle the password to ensure randomness
    random.shuffle(password)

    return "".join(password)


def convert_y_n_reply_to_bool(reply: str) -> bool:
    """
    Convert a 'y' or 'n' user input to a boolean value.

    Parameters:
        reply (str): User input ('y' or 'n').

    Returns:
        bool: True if 'y', False if 'n'.

    Raises:
        ValueError: If the input is not 'y' or 'n'.
    """
    if reply == "y":
        return True
    elif reply == "n":
        return False
    else:
        raise ValueError("Invalid answer. Only 'y' or 'n' is expected.")


def main() -> None:
    """
    Main function for the password generator script.

    Prompts the user for password criteria (length, inclusion of uppercase letters,
    numbers, and special characters) and generates a secure password based on the input.
    """
    # Prompt the user for password length
    password_length: int = int(input("Enter the length of the password: "))

    if password_length < 1:
        raise ValueError("Password length can't be less than 1.")

    # Prompt the user for inclusion options
    is_uppercase_included: bool = convert_y_n_reply_to_bool(input("Should we include uppercase letters? y/n: "))
    is_numbers_included: bool = convert_y_n_reply_to_bool(input("Should we include numbers? y/n: "))
    is_special_characters_included: bool = convert_y_n_reply_to_bool(
        input("Should we include special characters? y/n: "))

    # Generate the password
    generated_password: str = generate_password(
        password_length,
        is_uppercase_included,
        is_numbers_included,
        is_special_characters_included
    )

    # Display the generated password
    print("Generated password:\n", generated_password)


if __name__ == '__main__':
    main()
