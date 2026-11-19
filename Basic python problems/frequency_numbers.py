num = int(input("Enter a number here:"))

target = int(input("Enter your target number here:"))

count = 0

while num>0:
    digit = num % 10

    if digit == target:
        count = count + 1

    num = num // 10

print("frequency of target number is ", count , "times")