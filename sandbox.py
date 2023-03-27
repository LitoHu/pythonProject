"""write a program that asks the user for a password, with error-checking to repeat if the password doesn't meet a minimum length set by a variable.
The program should then print asterisks as long as the word.
Example: if the user enters Pythonista (10 characters), the program should print **********."""

COUNT = 6


def main():
    password = input("Enter your password: ")
    length_password = len(password)

    if length_password >= COUNT:
        print_astrisk(length_password)
    else:
        print("invalid passwords, please try again")


def print_astrisk(length_password):
    print("*" * length_password)


main()
