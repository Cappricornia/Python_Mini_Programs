# The Password program uses the if statement to simulate  the login procedure of a highly secure computer system.
# The program grants the user access if he or she enters the correct password.
# In the real world, it will be used some kind of cryptography to create a password validation system but this
# is just a simple fun way to see how it works :)

print("Welcome to Highlands Security Inc.\n")

password = input("Enter your password:")

if password == "secret":
    print("Access Granted")
    print("Welcome!")

else:
    print("Access Denied")


input("\n\nPress the enter key to exit.")

