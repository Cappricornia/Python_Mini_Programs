# Coffee Program

# How much coffee you need to stay awake? Until you receive the command "END",
# you need to read commands on different lines. According to the commands, you will print the number of
# coffees you need to stay awake during the daytime. If the count exceeds 5, print 'You need extra sleep'.
# The list of events can contain the following:
# •	"coding"
# •	"dog" or "cat"
# •	"movie"
# •	 Just ignore any other events
# Each event can be lowercase or uppercase. If it is lowercase, you need 1 coffee by event, and if it is
# uppercase, you need 2 coffees.
events = input()
event_lower = ['coding', 'movie', 'dog', 'cat']
event_upper = ['CODING', 'MOVIE', 'DOG', 'CAT']
coffee = 0

while events != "END":
    if events in event_lower:
        coffee += 1
    elif events in event_upper:
        coffee += 2
    events = input()

if coffee > 5:
    print("You need extra sleep!")
elif coffee == 1:
    print(f"You need {coffee} cup of coffee.")
else:
    print(f"You need {coffee} cups of coffee.")

