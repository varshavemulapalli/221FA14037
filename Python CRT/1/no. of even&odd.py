'''19.write a python A PROGRAM to read an integer as input and print the no. of even and odd digits present in that'''
number =int(input("Enter an integer: "))
even_count = 0
odd_count = 0

for digit in number:
    if digit.isdigit():
        if int(digit) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

print("Even digits:", even_count)
print("Odd digits:", odd_count) 
