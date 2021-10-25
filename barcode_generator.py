
# Write a program which prints all barcodes that consists only of odd numbers.


first_number = int(input("Please enter the first 4-digit number between 1000 and 9999:"))
second_number = int(input("Please enter the second 4-digit number between 1000 and 9999:"))
first_1 = 0
first_2 = 0
first_3 = 0
first_4 = 0
end_1 = 0
end_2 = 0
end_3 = 0
end_4 = 0

for index, digit in enumerate(str(first_number)):
    if index == 0:
        first_1 = int(digit)
    elif index == 1:
        first_2 = int(digit)
    elif index == 2:
        first_3 = int(digit)
    else:
        first_4 = int(digit)
for index_end, digit_end in enumerate(str(second_number)):
    if index_end == 0:
        end_1 = int(digit_end)
    elif index_end == 1:
        end_2 = int(digit_end)
    elif index_end == 2:
        end_3 = int(digit_end)
    else:
        end_4 = int(digit_end)
for a in range(first_1, end_1 + 1):
    for b in range(first_2, end_2 + 1):
        for c in range(first_3, end_3 + 1):
            for d in range(first_4, end_4 + 1):
                if a % 2 != 0 and b % 2 != 0 and c % 2 != 0 and d % 2 != 0:
                    print(f'{a}{b}{c}{d}', end=" ")


input("\n\nPress the enter key to exit")

