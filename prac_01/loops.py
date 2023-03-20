
start, end = 1, 20
for num in range(start, end + 1):
    if num % 2 != 0:
        print(num, end=" ");

"""a. count in 10s from 0 to 100"""
for i in range(0, 100, 10):
        print(i, end=' ');

"""count down from 20 to 1"""
for i in range(20, 0, -1):
    print(i, end=' ');

"""print n stars. Ask the user for a number, then print that many stars (*), all on one line"""
number_of_stars = int(input("Enter a number: "))
for i in range(number_of_stars):
    print("*", end="");

"""c.print n lines of increasing stars. Using the same number as above, print lines of increasing stars, starting at 1"""
"""n = int(input("Enter a number: "))
for i in range(1, n+1):
    for j in range(i):
        print("*", end="")
    print()
print()"""

number_of_stars = int(input("Enter a number: "))
for i in range(1, number_of_stars + 1, 1):
        print("*", * 1)
    print()
