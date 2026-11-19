# even and odd numbers counting

even_count = 0
odd_count = 0

for i in range(5):
    number=int(input("Enter your number:"))

    if number%2 == 0:
        even_count=even_count+1
    elif number%2 != 0:
        odd_count=odd_count+1


print(even_count)
print(odd_count)
