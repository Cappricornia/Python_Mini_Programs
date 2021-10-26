print("\nThe Easter Bread program\n\n")
print("Since it is Easter, you have decided to make some loaves of Easter bread and exchange them for eggs.\nThe Easter\
 Bread program will calculates how many loaves you can make with the budget you have.\nHere is the recipe for\
 one bread:\nEggs 1 pack\nFlour 1 kg\nMilk 0.250l\n\nThe price for 1 pack of eggs is 75% of the\
 price for 1 kg flour. The price for 1l milk is 25% more than the price for 1 kg flour.\nNotice that you need 0.250l\
 milk for one bread, and the calculated price is for 1l. Start cooking the loaves and keep making them until you have\
 enough budget.\nKeep in mind that:\n\n-->For every bread that you make, you will receive 3 colored eggs.\n-->For\
 every 3rd bread you make, you will lose some of your colored eggs after receiving the usual 3 colored eggs\
 for your bread.\nIn the end, it will be printed the loaves of bread you made, the eggs you have gathered,\
 and the money you have left.\n")


print("Enter your budget: ")
budget = float(input())
print("Enter price per 1kg flour: ")
flour_price_kg = float(input())
price_per_eggs = flour_price_kg * 0.75
price_per_litre_milk = flour_price_kg + (flour_price_kg * 0.25) # 1l milk milk for 4 breads
price_milk_per_250ml = price_per_litre_milk / 4
eggs_gathered = 0
made_bread = 0
bread_price = price_per_eggs + flour_price_kg + price_milk_per_250ml
while True:
    if budget >= bread_price:
        budget -= bread_price
        made_bread += 1
        eggs_gathered += 3
        if made_bread % 3 == 0:
            eggs_gathered -= made_bread - 2
    if budget < bread_price:
        break
print(f"You made {made_bread} loaves of Easter bread! Now you have {eggs_gathered} eggs and ${budget:.2f} left.")





