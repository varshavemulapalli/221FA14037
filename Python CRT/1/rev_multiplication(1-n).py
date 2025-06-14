'''9.write a python program to print reversed multipication table of 1 to n'''

n = int(input("Enter the value of n: "))
for num in range(1, n + 1):
    print(f"\nReversed Multiplication Table of {num}:")
    for i in range(10, 0, -1):
        print(f"{num} x {i} = {num * i}")
