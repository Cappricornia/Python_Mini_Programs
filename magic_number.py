# Magic number
# Write a program to check all possible combinations between two numbers.
# first_number - int in range [1...999]
# second_number - int in range[ bigger than first number...1000]
# magic_number - int in range[1...10000]

first_number = int(input())
second_number = int(input())
magic_number = int(input())
counter_combinations = 0

for one in range(first_number, second_number + 1):
    for two in range(first_number, second_number + 1):
        counter_combinations += 1
        if one + two == magic_number:
            print(f"Combination N:{counter_combinations} ({one} + {two} = {magic_number})")
            exit()

print(f"{counter_combinations} combinations - neither equals {magic_number}")
