# Number Between 1 and 100

# The program that reads different floating-point numbers from the console. When it receives a number between
# 1 and 100 inclusive, the program should stop reading and should print "The number {number} is between 1 and 100".


while True:
    current_num = float(input("Enter decimals or whole numbers, once you enter a number between 1 and 100 the\
 program will end and will display a funny message.\n"))
    if 1 <= current_num <= 100:
        print(f"The number {current_num} is between 1 and 100. You get {current_num} virtual kisses <>")
        break

