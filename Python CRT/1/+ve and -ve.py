'''1.write a python program to read the integer value as input from the user & check whether it is a positive number or negative number'''

Num=int(input("Enter the Integer: "))
#using if-else
if(Num>0):
    print(f"{Num} is +ve Number")
elif(Num<0):
    print(f"{Num} is -ve Number")
else:
    print(f"{Num} is 0")
#using ternary operator
Res="+ve Num" if (Num>0) else "-ve Number"
