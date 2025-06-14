'''write a python program to declare a list of words and declare tuple of words and map it to print the combined words '''
n=int(input("Enter no. of words that you would like to find : "))
list=['Marker','Water','Wrist','Bread','Class','Home','Jim','Black','Crack']
tuple=('Pen','Bottle','Watch','Jam','Room','theatre','Jam','Board','Jack')
i=1
while(i<=n):
    word=input("Enter the word : ")
    index=list.index(word)
    print(f"{word}-{tuple[index]}")
    i+=1