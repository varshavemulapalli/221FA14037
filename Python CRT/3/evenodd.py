'''
8. write a python program to:
input a lsit of numbers
create two new lists: one for even numbers , one for odd numbers.
display both lists '''    

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
even_numbers = []
odd_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers) 



