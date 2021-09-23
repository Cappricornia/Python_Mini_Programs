#Special Numbers

# write a program which reads an integer n and prints all special numbers from 1 to n.


print("Welcome to Special numbers!\n")

print("A number is special when the sum of its digits is 5, 7 or 11. If you see True, the number is special.")
end = int(input("Enter a number: "))
for num in range(1, end + 1):
    current_num = num
    sum = 0

    while current_num > 0:
        digit = current_num % 10
        sum += digit
        current_num = current_num // 10
    if sum == 5 or sum == 7 or sum == 11:
        print(f"{num} -> {True}")
    else:
        print(f"{num} -> {False}")