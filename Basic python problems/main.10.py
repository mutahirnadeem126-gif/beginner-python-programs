pos_sum = 0
neg_sum = 0

for i in range(10):
    number = int(input("Enter your numbers here:"))

    if number>0:
        pos_sum = pos_sum + number

    if number<0:
        neg_sum = neg_sum + number

    total_sum = pos_sum + neg_sum

print(f"the sum of positivr numbers is {pos_sum}")
print(f"the sum o negative number is {neg_sum}")
print(f"the sum of all numbers is {total_sum}")

# positive and negative number sum calculator