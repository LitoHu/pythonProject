
"""num_items = int(input("Number of items: "))
total_price = 0,
choice = total_price;
for i in range(num_items):
    item_price = float(input("Price of item: "))
    total_price += item_price

if total_price > 100:
    total_price *= 0.9

print(f"Total price for {num_items} items is ${total_price:.2f}")"""
num_items = int(input("Number of items: "))
#valide the price first, coz u don't want -1
while number_of_items < 0:
    print("Invalid input")
    number_of_items = int(inpu(f"Enter number "))