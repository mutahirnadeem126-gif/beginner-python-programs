num = int(input("Enter your number here:"))

reverse = 0
org_num = num

while num>0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("the reverse of the number is :",reverse)

if org_num == reverse:
    print("The number is palindrome")
else:
    print("The number is not palindrome")