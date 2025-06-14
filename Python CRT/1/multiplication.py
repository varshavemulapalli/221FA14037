'''6.write a python program to read an integer value from the user and print multiplication table of it. '''

Num=int(input("Enter the integer value : "))
print(f"Multiplication Table of {Num}:")
for i in range(1, 11):
    print(f"{Num} x {i} = {Num * i}")
    