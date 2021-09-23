# Patterns


rows = int(input("Enter a number: "))
for row in range(1, rows + 1):
    for col in range(0, row):
        print("*", end=" ")
    print()
for row in range(rows - 1, 0, -1):
    for col in range(0, row):
        print("*", end=" ")
    print()

