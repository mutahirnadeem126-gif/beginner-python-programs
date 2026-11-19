# sum of digits

num = int(input("enter a number here:"))
# used to handle nrgative numbers
num=abs(num)
total = 0

while num>0:
    digit = num % 10
    total = total + digit
    num = num // 10

print("Sum of digits:", total)



