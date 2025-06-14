''''write  a python program to read two integer values as input from the user and swap the numbers.'''


Num1=int(input("Enter the first number"))
Num2=int(input("Enter the second number"))
print("Num1 =",Num1)
print("Num2 =",Num2)
print("After Swapping :")
Num1,Num2=Num2,Num1
Temp=Num1
Num1=Num2
Num2=Temp
# Num1=10, Num2=20
Num1=Num1+Num2 # Num1=30
Num2=Num1-Num2 # Num2=10
Num1=Num1-Num2
print("Num1 =",Num1)
print("Num2 =",Num2)