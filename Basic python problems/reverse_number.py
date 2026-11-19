num = int(input("Enter your number here:"))

reverse = 0

while num>0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("the reverse of the number is :",reverse)