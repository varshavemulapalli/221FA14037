'''write a python program to read the size of list as input from the user and take a the ist elements also as input from the user and find the length of the list or
 maximum no or element present in the list and similarly the min element, the summation of elements and print the sorted list in ascending order'''
Size=int(input("Enter the Size of List :"))
Num=[]
for i in range(Size):
    Temp=int(input(f"Enter the Element at{i} index:"))
    Num.append(Temp)
print(f"Given List : {Num}")    
print("Maximum Element :",max(Num))
print("Minimum Element :",min(Num))
print("Summation  :",sum(Num))
print("Sorted List :",sorted(Num))