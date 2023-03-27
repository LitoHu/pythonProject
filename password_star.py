
"""write a program that asks the user for a password, with error-checking to repeat if the password doesn't meet a minimum length set by a variable.
The program should then print asterisks as long as the word.
Example: if the user enters Pythonista (10 characters), the program should print **********."""


"""constant must be on the top"""
def main():
    get_password()
    """
    Python function to get password, 
    check the number of password,
    print same number of "*" when number is bigger than 6,
    otherwise print "invalid passwords"
    """
def get_password():
    password = input("Enter your password: ")
    count = 6
    if len(password) >= count:
        print("*" * len(password))
    else:
        print("invalid passwords, please try again")
    """
    Refactor password program
    """
main()


