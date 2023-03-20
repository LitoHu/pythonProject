
"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32
        print("The temperature in Fahrenheit is: {:.2f}".format(fahrenheit))
    elif choice == "F":
        fahrenheit = float(input("fahrenheit: "))
        celsius = 5 * (fahrenheit - 32) / 9.0
        print("The temperature in Celsius is: {:.2f}".format(celsius))
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")