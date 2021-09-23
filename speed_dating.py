# Speed Dating
# The program will find all possible combination between clients of the restaurant so every man to meet every women
# If no free table, the program will break

print("Welcome to Speed Dating Game! \n"
"Every client will receive a number ticket and each man will meet each woman and vice versa for 3 minutes.\n"
"If they like each other in the end of the game we can provide their contacts confidentially.\n")

print("Please enter men number between 1 and 100:")
men = int(input())
print("Please enter women number between 1 and 100:")
women = int(input())
print("Please enter table number between 1 and 100. Each table has 2 seats.")
tables = int(input())

for man in range(1, men + 1):
    for woman in range(1,  women + 1):
        print(f"Man No.{man} <-> Woman No.{woman}")

input("\n\nPress the enter key to exit")











