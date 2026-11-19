pos = 0
neg = 0
zero = 0
for i in range(10):
    number = int(input("Enter your numbers:"))

    if number > 0:
        pos = pos + 1

    elif number < 0:
        neg = neg + 1
    elif number == 0:
        zero = zero + 1

print(f"There are {pos} positive numbers")

print(f"there are {neg} negative numbers")

print(f"There are {zero} zero numbers")