# Count Sheep Program

# You can try counting sheep if you can't sleep!

sheep = int(input("Please enter a positive number:\t"))
for num_sheep in range(1, sheep + 1):
    print(f"{num_sheep} sheep...", end="")
