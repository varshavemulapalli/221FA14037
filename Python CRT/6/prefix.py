'''Write a python program to take name as input including prefix(Mr/Ms)
print the gender classification of the name on the bases of prefix'''

str=input("enter the name: ")
if str.startswith("Mr"):
    print("Male")
else str.startswith("Ms"):
    print("female")
