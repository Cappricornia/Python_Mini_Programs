# The Special Car Number Generator

print("The Special Car Number Generator\n\n")
print("Each car number consist of 4 digits.\nThe car number is special if the following conditions are met:\n")
print("---> if the number starts with even number it should end with odd number\n---> if the number starts with odd\
 number it should end with even number\n---> if the first number in number is bigger than the last one\n---> The sum of\
 second and third number should be an even number\n")

print("Please enter first number between 1 and 9:")
first = int(input())
print("Please enter second number between 1 and 9:")
second = int(input())
sum_middle = 0
for a in range(first, second + 1):
    for b in range(first, second + 1):
        for c in range(first, second + 1):
            for d in range(first, second + 1):
                sum_middle = b + c
                if a > d and sum_middle % 2 == 0:
                    if a % 2 == 0 and d % 2 != 0 or a % 2 != 0 and d % 2 == 0:
                        print(f"{a}{b}{c}{d}|", end= " ")


input("\n\nPress the enter key to exit")
