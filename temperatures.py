
MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()
def main():
    while choice != "Q":
    celsius_to_fahrenheit()
    print("The temperature in Fahrenheit is: {:.2f}".format(choice));
    fahrenheit_to_celsius()
    print("The temperature in Celsius is: {:.2f}".format(choice))
    otherwise()
print(MENU)
choice = input(">>> ").upper()
print("Thank you.")

def celsius_to_fahrenheit():
    choice = input(">>> ").upper()
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32
"""
convert celsius to fahrenheit
"""

def fahrenheit_to_celsius():
    choice = input(">>> ").upper()
    if choice == "F":
        fahrenheit = float(input("fahrenheit: "))
        celsius = 5 * (fahrenheit - 32) / 9.0
"""
convert celsius to fahrenheit
"""

def otherwise():
    choice = input(">>> ").upper()
    if choice == "Q":
        print("Invalid option")
"""
end the program if the user choose
"""





