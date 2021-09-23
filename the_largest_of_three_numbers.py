# Write a program that receives three whole numbers and prints the largest one.


import sys
first_num = int(input("Please enter the first number:"))
second_num = int(input("Please enter the second number:"))
third_num = int(input("Please enter the third number:"))
max_num = -sys.maxsize
if first_num > max_num:
    max_num = first_num
if second_num > max_num:
    max_num = second_num
if third_num > max_num:
    max_num = third_num
print("The largest number is:",max_num)


