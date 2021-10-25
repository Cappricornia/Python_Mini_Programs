# Birthday wishes Program
# def() function
# Demonstrates keyword arguments and default parameter values


# positional parameters
def birthday1(name,age):
    print("Happy Birthday,", name, "!", "I hear you're", age, "today.\n")

# parameters with default values
def birthday2(name = "Merry", age = 23):
    print("Happy Birthday,", name, "!", "I hear you're", age, "today.\n")


birthday1("Merry", 23)
birthday1(23,"Merry")
birthday1(name = "Merry", age = 23)
birthday1(age = 23, name = "Merry")

birthday2()
birthday2(name="Ben")
birthday2(age = 12)
birthday2(name = "Ben", age = 12)
birthday2("Ben", 12)

input("\n\nPress the enter key to exit.")