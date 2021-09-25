# Is Your Number a Prime Number
# This simple program will check if a number entered by a user is a prime number

number = int(input("Enter a number: "))

if number > 1:
    for i in range(2, number):
        if number % i == 0:
            print("Not Prime")
            break
    else:
        print('Prime')

