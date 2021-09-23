# Find the Capitals program
# Write a program that takes a single string and prints a list of all the capital letters indices.

word = input("What's on your mind? I can show you all capital letters as indices. Go ahead..type something...\n ")
capitals = []
for index,letter in enumerate(word):
    if 65 <= ord(letter) <= 90:
        capitals += [index]
print(capitals)