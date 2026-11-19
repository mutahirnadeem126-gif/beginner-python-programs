num = int(input("enter your number here:"))
product = 1

while num>0:
    digit = num % 10
    product = product * digit
    num = num // 10

print("product of dits is :" , product)
