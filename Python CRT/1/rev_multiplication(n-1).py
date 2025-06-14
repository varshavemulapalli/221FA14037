'''10.write python program to print the reversed multiplication from n to 1'''

n = int(input("Enter the value of n: "))
for num in range(n, 0, -1):
    print(f"\nReversed Multiplication Table of {num}:")
    for i in range(10, 0, -1):
        print(f"{num} x {i} = {num * i}")
