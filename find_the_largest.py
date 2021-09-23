# Find the largest number

#Print the largest number that can be formed from the digits of the given number.

number = input("Please enter a number: ")
my_list = []
reversed = 0
for num in number:
    my_list += [num]
    my_list.sort(reverse=True)
    reversed = int(''.join(my_list))
print(reversed)


