
""""# get name
name = input("Enter name: ")
# Display menu
choice = ''
#get choice
while choice != 'Q':
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")
    if choice == 'H':
        print(f"Hello {name}")
    elif choice == 'G':
        print(f"Goodbye {name}")
    elif choice == 'Q':
        print("Finished.")
    else:
        print("Invalid choice")"""

menu = "(H)eLlo\n(G)goodbye\n(Q)uit"

name = input("Enter name:")

print(menu)
choice = input(">>>").upper()
while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")
    print(menu)
    Choice = input(">›>").upper()
print("Finished")