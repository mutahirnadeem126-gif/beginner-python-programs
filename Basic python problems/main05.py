largest = None
sec_largest = None

for i in range(5):
    num = int(input("Enter a number: "))

    if largest is None:
        largest = num

    elif num > largest:
        sec_largest = largest
        largest = num

    elif sec_largest is None or num > sec_largest:
        if num != largest:
            sec_largest = num

if sec_largest is not None:
    print("Second Largest:", sec_largest)
else:
    print("Second largest number does not exist")