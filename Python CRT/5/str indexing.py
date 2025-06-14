a=10
b='10'
print(a is b)'''
'''
Str="Python"
print(f"Length of{str} is {len(Str)}")
#Accessing without index
for i in Str:
    print(i,end=" ")
print()
#Accessing with index
for i in range(len(Str)):
    print(Str[i],end=" ")

Str1="Students"
Str1[4]= "i"
for c in Str1:
    print(c)
