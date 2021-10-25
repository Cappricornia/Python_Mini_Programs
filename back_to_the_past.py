print("Back to the past\nYou get an inheritance and a time machine and you want to go back to 1800.\nWill you have\
 enough money to survive if you are back in time?\n")

print("You are 18 years old.\nAnnual expenses:\nper ever year: $12 000;\nper odd year: $12 000 + 50 * your current age")
print("\nEnter inheritance between 1.00 and 1 000 000.00: ")
inheritance = float(input())
print("Enter year between 1801 and 1900: ")
year_end = int(input())
age = 18
year_start = 1800
even_expenses = 12000
for y in range(year_start, year_end + 1):
    if year_start % 2 == 0:
        # expenses for even years
        inheritance -= even_expenses
    else:
        # expenses for odd years
        inheritance -= even_expenses + age * 50
    age += 1
    year_start += 1
if inheritance < 0:
    print(f"You will need {abs(inheritance):.2f} dollars to survive.")
else:
    print(f"Yes! You will live a carefree life and will have {inheritance:.2f} dollars left.")


input("\n\nPress the enter key to exit")


