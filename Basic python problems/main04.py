# largest number calculator

num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))
num3 = int(input("Enter number 3:"))
num4 = int(input("Enter number 4:"))
num5 = int(input("Enter number 5:"))

largest = num1

if num1 > largest:
    largest = num1
if num2 > largest:
    largest = num2
if num3 > largest:
    largest = num3
if num4 > largest:
    largest = num4
if num5 > largest:
    largest = num5

print(f"The largest number is {largest}")