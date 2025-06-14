'''6. write a python program to:
take a list of toy names(some repeated).
Remove duplicates.
sort and display th efinal toy list to pack.'''


List=['cars','cars', 'jeep','jeep','aeroplane',]
print("Original List:")
print(List)
New_List=[]
for i in List:
    if i not in New_List:
        New_List.append(i)
print(New_List)  