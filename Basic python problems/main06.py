smallest = None
sec_smallest = None

for i in range(5):
    num = int(input("Enter your number:"))

    if smallest is None:
        smallest = num

    elif smallest > num:
        sec_smallest=smallest
        smallest = num
    elif sec_smallest is None or num < sec_smallest:
            if num != smallest:
                sec_smallest = num

if sec_smallest is not None:
    print("The second smallest is",sec_smallest)
else:
    print("second smallest dosen,t exsist")


print("smallest is",smallest)