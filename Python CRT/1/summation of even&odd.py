'''20.write a python program to read an integer value from user and then find summation of even digits and odd digits present in that particular number'''
number = input("Enter an integer: ")
even_sum = 0
odd_sum = 0

for digit in number:
    if digit.isdigit():
        if int(digit) % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)

print("Sum of even digits:", even_sum)
print("Sum of odd digits:", odd_sum)  
