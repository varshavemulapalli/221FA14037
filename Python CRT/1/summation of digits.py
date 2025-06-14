'''18.write a python program to read the integer value as input from user and find the summation of digits
sample 
enter integer value : 18715
1+8+7+1+5
o/p: 22'''

Num=int(input("Enter the value of Num:"))
DigitSum=0
Rem=0
while(Num!=0):
    Rem=Num%10
    DigitSum=DigitSum+Rem 
    Num=Num//10
print(f"Summation is {DigitSum}")
