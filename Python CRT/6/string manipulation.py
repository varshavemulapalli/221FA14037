'''write a python program to read a sentence as an input from the user and print the list of words from the sentence'''
'''sentence=input("Enter the sentence :")
list=sentence.split( )
print(list)
for word in range(len(sentence)):
    if sentene[ch+1]==" ":
'''

'''write the python program to read the string as input from user 
1) reverse the string
2) covert the sting into lowercase
3)convert the string into upper case
4)convert the characters of string to lower case if it is in uppercase and conevert the string into uppercase if it is in lowercase
5)check if the string is starting with letter 'a' 
6) print the count of the character 'a' from the given string 
7)replace all 'p' to letter 'j'
'''
'''
str=input("Enter the string : ")
print(str[::-1])
print(str.lower())
print(str.upper())
print(str.swapcase())
print(str.startswith('P'))
print(str.count('P'))
str=str.lower()
print(str.replace('p','j'))
'''


'''write the python program to read the list of characters from the user and convert it into a word and print'''
'''Size=int(input("Enter the length of list :"))
Char_list=[]
for i in range(Size):
    ch=input("Enter the characters:")
    Char_list.append(ch)
print(Char_list)    
Str="-".join(Char_list)
print(Str)'''




'''str="python program"
print(str.capitalize())
print(str.title())
print(str.casefold())
print(str.startswith('p'))
print(str.find('o'))
print("Hi".center(15,"*"))
'''
'''write a python program to read a string as input from user 
1)print count uppercase letters
2) print count lowercase letters
3)print the numeric values
4)print the count of special characters'''
'''
str=input("Enter the string :")
Uppercase_Alpha=0
Lowercase_Alpha=0
Numeric=0
Special_char=0
for ch in str:
    if ch.isupper():
        Uppercase_Alpha+=1
    elif ch.islower():
        Lowercase_Alpha+=1
    elif ch.isdigit():
         Numeric+=1
else:
   Special_char+=1     
print(f"Count of Upper case letters :{Uppercase_Alpha}")
print(f"Count of Lower case letters :{Lowercase_Alpha}")
print(f"Count of Numeric Values :{Numeric}")
print(f"Count of Special Characters :{Special_char}")
'''
