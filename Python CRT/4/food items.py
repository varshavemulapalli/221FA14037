#write a program 
#1) to display a menu of food items (list)
#2)create a tuple of prices with respect to food items list
#3)read the input from user for ordering the food including the Quantity
#if it exists in the menu -- confirm order, if not print a message -- order something else
#4)While billing , read no., feedback,read tip amount
#5)add 18% gst to the bill and print the bill if bill > 0


n=int(input("Enter no.of items : "))
list=['Shawarama','Panipuri','Waffle','Biryani','Butterchicken']
tuple=('150/-','30/-','100/-','300/-','220/-')
print("Menu Items:", list)
print("Prices:", tuple)
i=1
while(i<=n):
    item=input("Enter the item : ")
    index=list.index(item)
    print(f"{item}-{tuple[index]}")
    i+=1
