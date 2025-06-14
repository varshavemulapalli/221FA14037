'''21.write a python program to read an integer value as input from user and find  no. of zeros present in the user entered numbers'''
number = input("Enter a number: ")
zero_count = 0

for digit in number:
    if digit == '0':
        zero_count += 1

print("Number of zeroes:",zero_count)