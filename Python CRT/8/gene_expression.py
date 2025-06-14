'''"Underexpressed" (<5)
"normal" (5 to 15)
"overexpressed" (>15)
sample input
Enter the count of data :5
user entered list : [3.2,5,5,12.4,16.7,]
'''
n=int(input("Enter the size :"))
list=[]
list1=[]
for i in range(n):
    temp=float(input("Enter the GE value :"))
    list.append(temp)
for i in list:
    if i<5:
        list1.append("Underexpressed")
    elif i>=5 and i<=15:
        list1.append("Normal")
    else:
        list1.append("Overexpressed")
print(list1)
