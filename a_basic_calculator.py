# A Basic Calculator

number_one = float(input("Enter first number: "))
operator = input("Enter operator: ")
number_two = float(input("Enter second number: "))

if operator == "+":
    print("Result:",number_one + number_two)
elif operator == "-":
    print("Result:",number_one - number_two)
elif operator == "/":
    print("Result:",number_one / number_two)
elif operator == "*":
    print("Result:",number_one * number_two)
else:
    print("Invalid operator")