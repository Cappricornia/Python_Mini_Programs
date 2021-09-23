#  Demonstrating slicing  tuples

inventory = ("fork",
             "knife",
             "spoon",
             "plate")
index = int(input("\nEnter the index number for an item in inventory: "))
print("At index", index, "is", inventory[index])

# SLICING Tuples

# display a slice

start = int(input("\nEnter the index number to begin a slice:"))
finish = int(input("\nEnter the index number to end a slice:"))
print(inventory[start:finish])
print(inventory[:1])
print(inventory[:2])
print(inventory[:3])
print(inventory[::])

input("\nPress enter key to continue")