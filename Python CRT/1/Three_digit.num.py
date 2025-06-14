'''4.write a python program to read the integer value as input from the user & check whether it is a three digit  number or not three digit number'''

num = int(input("Enter an integer: "))
if -999 <= num <= -100 or 100 <= num <= 999:
    print(f"{num} is a three-digit number.")
else:
    print(f"{num} is not a three-digit number.")
