'''5. write a python program to read amount as input from the user & print  the number of notes required on Indian currency dimesion
sample test case :
Enter the Amount : 3864/-
2000------->1
500-------->3
200-------->1
100-------->1
50--------->1
20--------->0
10--------->1
2---------->2

'''
amount = int(input("Enter the Amount: "))
denominations = [2000, 500, 200, 100, 50, 20, 10, 5,2]
for note in denominations:
    count = amount // note  
    amount %= note         
    print(f"{note}-------->{count}")

#alternate code
Amount=int(input("Enter the amount "))
print("2000------->",Amount//2000)
Amount=Amount%2000
print("500-------->",Amount//500)
Amount=Amount%500
print("200-------->",Amount//200)
Amount=Amount%200
print("100-------->",Amount//100)
Amount=Amount%100
print("50-------->",Amount//50)
Amount=Amount%50
print("20-------->",Amount//20)
Amount=Amount%20
print("10-------->",Amount//10)
Amount=Amount%10
print("5-------->",Amount//5)
Amount=Amount%5
print("2-------->",Amount//2)
Amount=Amount%2
print("1-------->",Amount//1)
Amount=Amount%1
