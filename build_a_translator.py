# A simple Translator

# We can create a very simple language - Bubu Language
# convert vowels to --> b


def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation += "B"
            else:
                translation += "b"
        else:
            translation += letter
    return translation

print(translate(input("Please enter a phrase: ")))

input("\n\nPress the enter key to exit")
