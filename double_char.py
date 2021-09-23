#Double Char program

# The program will print each character of the string twice. For example, is the user enters "Mamma mia"
# the output will be MMaammmmaa  mmiiaa!!


user_sentence = input("Enter a word or a sentence: ")
new_string = ""
for char in user_sentence:
    new_string += char * 2
print(new_string)



