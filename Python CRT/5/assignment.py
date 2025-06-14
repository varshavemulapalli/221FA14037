'''
Write a python program to read the string as input from the user
a) print the string as a list of individual characters'''
'''
str = input("Enter a string: ")
char_list = [char for char in str]
print("List of characters:", char_list)
'''
'''b) find the length of the String'''
'''
str = input("Enter a string: ")
length = 0
for _ in str:
    length += 1
print("Length of the string:", length)
'''
'''c) find the minimum element after converting string into list'''
'''
str = input("Enter a string: ")
min_char = char_list[0]
for char in char_list:
    if char < min_char:
        min_char = char
print("Minimum element in the list:", min_char)
'''
'''d) find the number of spaces present in the string without using any built-in methods or function'''
'''
str = input("Enter a string: ")
space = 0
for char in str:
    if char == ' ':
        space += 1
print("Number of spaces:", space)
'''