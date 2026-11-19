even_sum = 0
odd_sum = 0

even_count = 0
odd_count = 0

for i in range(10):
    num = int(input("Enter your number here:"))

    if num % 2 == 0:
        even_sum = even_sum + num
        even_count = even_count + 1

    if num % 2 != 0:
        odd_sum = odd_sum + num
        odd_count = odd_count + 1


print(f"the sum of even number is {even_sum}")
print(f"the sum of odd numbers is {odd_sum}")

print(f"There are total {even_count} even numbers")
print(f"There are total {odd_count} odd numbers")