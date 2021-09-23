# Basic digital clock2 HH:MM:SS

for hour in range(0, 24):
    for minute in range(0, 60):
        for second in range(0, 60):
            print(f"{hour} : {minute:02d} : {second:02d}")