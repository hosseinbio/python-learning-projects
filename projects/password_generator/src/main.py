import random
import string
from typing import List, Optional


def generate_random_password(
    length: int = 8, include_numbers: bool = False, include_symbols: bool = False
) -> str:
    characters: str = string.ascii_letters
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    return "".join(random.choice(characters) for _ in range(length))


def generate_memorable_password(
    no_of_words: int = 5,
    separator: str = "-",
    capitalization: bool = False,
    vocabulary: Optional[List[str]] = None,
) -> str:

    if vocabulary is None:
        vocabulary = [
            "organ",
            "hair",
            "pest",
            "define",
            "tendency",
            "test",
            "merit",
            "dairy",
            "slant",
            "country",
            "freshman",
            "offspring",
            "choose",
            "mill",
            "forbid",
        ]

    if no_of_words <= len(vocabulary):
        password_words = random.sample(vocabulary, no_of_words)
    else:
        password_words = random.choices(vocabulary, k=no_of_words)

    if capitalization:
        password_words = [word.capitalize() for word in password_words]

    password = separator.join(password_words)

    return password


def generate_pin(length: int = 4) -> str:
    password = "".join(random.choice(string.digits) for _ in range(length))
    return password


def main():
    """
    The main function to generate the requested password
    """

    print("Welcome to Password Generator!")
    print("To generate a random password press 1")
    print("To generate a memorable password press 2")
    print("To print a PIN press 3")
    print("And to quit the program press 'q'")

    while True:
        choice = input("Please choose: ").lower()
        if choice in ("1", "2", "3"):
            break
        elif choice == "q":
            return None
        else:
            print("Wrong input!")

    if choice == "1":
        password = generate_random_password()
    elif choice == "2":
        password = generate_memorable_password()
    elif choice == "3":
        password = generate_pin()
    elif choice.lower() == "q":
        return None

    return password


if __name__ == "__main__":
    generated_pass = main()
    if generated_pass:
        print(generated_pass)
