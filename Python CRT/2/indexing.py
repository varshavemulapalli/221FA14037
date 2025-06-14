'''
Num_list=[10,20,30,40,50,60,70,80,90]
print(Num_list)
print("Accessing the list Elements using +ve indexing")
print(Num_list[0])
print(Num_list[1])
print(Num_list[2])
print(Num_list[3])
print(Num_list[4])
print(Num_list[5])
print(Num_list[6])
print(Num_list[7])
print(Num_list[8])
print("Accessing the list Elements using -ve indexing")
print(Num_list[-9])
print(Num_list[-8])
print(Num_list[-7])
print(Num_list[-6])
print(Num_list[-5])
print(Num_list[-4])
print(Num_list[-3])
print(Num_list[-2])
print(Num_list[-1])
'''

Num_list=[10,20,30,40,50,60,70,80,90]
print("Accesssing the list Elements using for loop without indexing")
for i in Num_list:
    print(i)
print("Accessing the list Elements using for loop with indexing")
#range(start,stop,stepsize),range(start,stop),range(stop)
for i in range (len(Num_list)):
    print(Num_list[i])
print("Accessing the list Elements using while loop")
i=0
while(i<len(Num_list)):
    print(Num_list[i])
    i+=1
    