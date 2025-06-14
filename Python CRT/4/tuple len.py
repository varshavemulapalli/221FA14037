'''write a python program to create a tuple of names and print the original tuple and print the names which has a length of 5 from the tuple'''

names_tuple = ("Alice", "David", "Sarah", "Tommy", "Chris", "John", "Maria", "James", "Emily", "Steve")

print("Original Tuple of Names:")
print(names_tuple)

print("Names with length 5:")
for name in names_tuple:
    if len(name) == 5:
        print(name)