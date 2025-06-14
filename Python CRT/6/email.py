'''WRITE a python program to read mail id as input from user and print username,organisation name based on mail id (name@org.com)'''
email = input("Enter your email : ")
list=email.split('@')
print(f"User Name : {list[0]}")
org=list[1]
list=org.split('.')
print(f"org name :{list[0]}")