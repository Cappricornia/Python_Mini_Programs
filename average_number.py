# Calculate The Average Number!
# Find the average of three numbers


print("Welcome to Calculate The Average Number!Please enter below 3 numbers:\n\n")
total_number = 3

print("Please enter the first number:\n")
number_one = int(input())
print("Please enter the second number:\n")
number_two = int(input())
print("Please enter the third number:\n")
number_three = int(input())
sum_numbers = 0

sum_numbers += number_one + number_two + number_three
average_number = sum_numbers / total_number
print(f"The average number is: {average_number:.2f}")

input("\n\nPress the enter key to exit")

