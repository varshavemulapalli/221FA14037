'''count the DNA Bases like a pro
count how many times each bases (A,T,G,C) appears in a DNA string.
enter the sample base values : "ATGCATAGCAGTGA"
{'A:5','T:3','G:4','C:2'}
'''

s=input("enter the base sequence : ")
A,T,G,C=0,0,0,0
sequence={1:'A',2:'C',3:'T',4:'G'}
for i in s:
    if i in sequence[1]:
        A+=1
    elif i in sequence[2]:
        C+=1
    elif i in sequence[3]:
        T+=1
    elif i in sequence[4]:
        G+=1
base={'A':A,'T':T,'G':G,'C':C}
print(base)
'''
n=input("Enter the DNA Sample: ")
dna={'A':n.count('A'),'T':n.count('T'),'G':n.count('G'),'C':n.count('C')}
print(dna)
'''
    
