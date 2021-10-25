print("\nWho is the Best player?\n\nWho is the player with max goals and if he made a 'hat trick' -  a player scoring\
 three goals in a game. If a player has scored 10 or more goals the game should STOP.")

print("Please see the example below and enter the information in the following order\n\nExample input No.1:\n\nNeymar\n2\
\nRonaldo\n1\nMessi\n3\nEND")

print("\n\nNow enter the data based on the example above:\n")
player_name = input()
max_goals = 0
best_player = ""
while not player_name == "END":
    current_goal = int(input())
    if current_goal > max_goals:
        max_goals = current_goal
        best_player = player_name
    if current_goal >= 10:
        break
    player_name = input()
print(f"{best_player} is the best player!")
if max_goals >= 3:
    print(f"He has scored {max_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {max_goals} goals.")


input("\n\nPress the enter key to exit")