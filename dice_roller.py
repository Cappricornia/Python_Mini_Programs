# Dice Roller
# The program simulates the roll of two, six-sided dice. It displays the value of each and their total.
# The program uses functions that generate random numbers.


# generate random numbers 1- 6

import random

die1 = random.randint(1, 6)
die2 = random.randrange(6) + 1

total = die1 + die2

print("You rolled a", die1, "and a", die2, "for a total of", total)

input("\n\nPress the enter key to exit.")