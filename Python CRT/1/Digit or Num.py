'''2.write a python program to read the integer value as input from the user & check whether it is a digit or  number'''

Num=int(input("Enter the Integer value :"))
#using if-else
if(Num>=-9 and Num<=9):
    print(f"{Num} is Digit")
else:
    print(f"{Num} is Number")
#ternary
Result="Digit"if (Num>=-9 and Num<=9) else "Number"
print(f"{Num} is {Result}")
