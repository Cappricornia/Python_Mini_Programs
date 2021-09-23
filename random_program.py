# The Random program uses sequence indexing to directly access random character in a string.
# The program picks a random position from the string "index", and prints the letter and the position number.
# The program will do this 10 times.

# Random Access
# Demonstrate string indexing
import random

word = "pancake"

print("The word is:", word, "\n")

high = len(word)
low = -len(word)

for i in range(10):
    position = random.randrange(low, high)
    print("word[", position,"]\t", word[position])

input("\n\nPress the enter key to exit.")

