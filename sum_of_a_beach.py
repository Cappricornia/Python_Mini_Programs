# Beach Words Program
# The given string calculates how many times the words
# "Sand", "Water", "Fish", and "Sun" appear (case insensitive).

my_string = "BeachandhghgsandAndFishbutalsoSunsunandWaTer"
my_string = my_string.lower()
words = ["sand", "water", "fish", "sun"]
counter = 0
for word in words:
    if word in my_string:
      find_word = my_string.count(word)
      counter += find_word
print("Some or all of the words 'Sand', 'Water', 'Fish, and 'Sun' appear", counter,"times.")





