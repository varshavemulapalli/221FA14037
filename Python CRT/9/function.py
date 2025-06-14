'''

#functions
def Display_prog():
    #function declaration
    print("Programming Languages")
    print("Java-Script")
    print("Python")
    print("SQL")
    print("C")
    print("C++")
    #function call
    Display_prog()
    Display_prog()
    Display_prog()
    Display_prog()
    Display_prog()
    Display_prog()
'''

'''
def display():
    return "Hey...!I'm the zero Arg function ....!"
Res=display()
print(Res)
def NameofFunction(name):
    return f"Hey..!T'm the one Arg Function called by {name }"
Res1=NameofFunction("Kavya")
print(Res1)
'''



'''write a python program to check whether the user given integer is evenor odd using functions'''
'''
def Even_odd(Num):
    if(Num%2==0):
        print(f"{Num} is Even")
    else:
        print(f"{Num} is odd")
Even_odd(10)
Even_odd(15)
Even_odd(32)
Even_odd(22)
Even_odd(56)
Even_odd(12)
Even_odd(21)
'''



'''write a python program to check whether the user given number is prime number or not using functions(return)'''
'''
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True
n = int(input("Enter a number: "))
if is_prime(n):
    print(n, "is a prime number")
else:
    print(n, "is not a prime number")
'''



'''write the python program to build a function which prints a multiplication table of n  '''
'''
def print_multiplication_table(n):
    print(f"Multiplication Table of {n}:")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
num = int(input("Enter a number to print its multiplication table: "))
print_multiplication_table(num)
'''
    