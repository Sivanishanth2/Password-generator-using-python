#Python project for a password generator

import random
import string


def generate_password(length):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    all_chars = lower + upper + digits + symbols

    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password


def main():

    while True:
        try:
            length = int(input("Enter the length of the password: "))
            if length <= 0:
                print("Please enter a valid integer for password length.")
                continue

            password = generate_password(length)


            print("Your generated password is:", password)
            break

        except ValueError:
            print("Invalid input. Please enter a valid integer for password length.")


if __name__ == "__main__":
    main()

