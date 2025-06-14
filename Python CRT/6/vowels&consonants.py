'''write a python program to read a string as input from user and print count of
1)print the count of uppercase vowels
2)print the count of lowercase vowels
3)print the count of upppercase consonants
4)print the count of lowercase consonants'''

str=input("Enter the string :")
U_Vowels,L_Vowels,U_Consonants,L_Consonants=0,0,0,0
for ch in str:
    if(ch.isalpha() and ch.isupper()):
        if ch in 'AEIOU':
            U_Vowels+=1
        else:
            U_Consonants+=1
    if(ch.isalpha() and ch.islower()):
        if ch in 'aeiou':
            L_Vowels+=1
        else:
            L_Consonants+=1
print(f"Upper Case Vowel counts :{U_Vowels}")
print(f"Lower Case Vowel counts :{L_Vowels}")
print(f"Upper Case Consonants counts :{U_Consonants}")
print(f"Lower Case Consonants counts :{L_Consonants}")




'''write a python program to print uppercase alphabets from A to Z'''
'''
for i in range(1,27):
    print(chr(i+64),"---->",i+64)
print("-----------------")
for i in range(1,27):
    print(chr(i+96),"---->",i+96)
'''