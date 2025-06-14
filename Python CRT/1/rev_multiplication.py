'''8.write a python program to print reversed multiplication table of n '''

n = int(input("Enter a number: "))
print(f"Reversed Multiplication Table of {n}:")
for i in range(10, 0, -1):
    print(f"{n} x {i} = {n * i}")
