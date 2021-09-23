# A new French fancy restaurant - Maitre D' asks how much money you slip your host. If you give 0 euros,
# you are ignored. If you give some less than 5 euro you need to wait for a while,
# if 5 or more then your table is waiting.

print("Welcome to the Chateau D' Mongo")
print("Unfortunately, we are quite full this evening.\n")

tip = int(input("How many euros do you slip the Maitre D'?"))
if tip >= 5:
    print("Ah, I am reminded of a table. Right this way, please.")
elif 0 < tip < 5:
    print("Please, seat. It may be a while.")
else:
    print("Please call us in advance and we will try to accommodate you next time.")

input("\n\nPress the enter key to exit.")