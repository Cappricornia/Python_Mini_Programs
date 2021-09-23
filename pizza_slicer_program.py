# The Pizza Slicer program
# Demonstrate string slicing

word = "pizza"

print(
    """
        Slicing 'Cheat Sheet'
        
          0   1   2   3   4   
        +---+---+---+---+---+
        | p | i | z | z | a |
        +---+---+---+---+---+
         -5  -4  -3  -2  -1
    
    """
)

start = None

while start != "":
    start = (input("\nStart: "))

    if start:  # is start = True
        start = int(start)

        finish = int(input("Finish:"))

        print("word[", start, ":", finish,"] is", end=" ")
        print(word[start:finish])

input("\n\nPress the enter key to exit. ")

