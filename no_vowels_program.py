# The No vowels program
# The program takes a message from the user and prints it, minus any vowels.
# What the program does is to to create a series of new strings.

message = input("Enter a message:")

new_message = ""
VOWELS = "aeiou"

print()
for letter in message:
    if letter.lower() not in VOWELS:
        new_message += letter
        print("A new string has been created:", new_message)

print("\nYOUR MESSAGE WITHOUT VOWELS IS:", new_message)

input("\n\nPress the enter key to exit.")

