# Emergency grab bag
# Demonstrating tuples

# create a tuple with some items and display with a for loop

emergency_grab_bag = ("flashlight",
             "batteries",
             "water & snacks",
             "phone charger & battery bank",
             "first aid kit")
print("Your items:")
for index, item in enumerate(emergency_grab_bag):
    print(index + 1, item)

input("\nPress the enter key to continue.")

print("You have", len(emergency_grab_bag), "items in your emergency grab bag.")


input("\n\nPress the enter key to exit")




