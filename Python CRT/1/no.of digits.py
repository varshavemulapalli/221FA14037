'''17. to read an integer value from user and print no. of digits present in that number
sample test case
Enter the Integer value : 18715
output : 5 digits
18715----->5
1871------>1
187------->7
18-------->8
1--------->1
0'''

Num=int(input("Enter the value of Num :"))
Temp=Num
DigitCount=0
while(Num!=0):
    Num=Num//10
    DigitCount+=1#DigitCount=DigitCount+1
print(f"{Temp} has {DigitCount} digits")
