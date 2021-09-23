# Reverse Text Generator

text = input("Please enter your text: ")

for i in range(len(text)-1, -1, -1):
    print(text[i], end="")

