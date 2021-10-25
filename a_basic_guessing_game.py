# A Basic Guessing Game
# We have a secret word stored in our program. The user should guess the word and if not to enter a new guess again
# guess limit 3 times

secret_word = "lollipop"
your_guess = ""
guess_counter = 0
limit_guess = 3
no_more_guesses = False

while not your_guess == secret_word and not(no_more_guesses):
    if guess_counter < limit_guess:
        your_guess = input("Enter guess: ")
        guess_counter += 1
    else:
        no_more_guesses = True

if no_more_guesses:
    print("Sorry! You lose!")
else:
    print("You win!")

input("\n\nPress the enter key to exit")
