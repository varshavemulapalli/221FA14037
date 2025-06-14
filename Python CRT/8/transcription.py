'''write a loop to convert a DNA string to its RNA form
Enter the DNA String :"ATCGTAC"
Converted String:"AUCGUAC"'''
DNA = input("Enter the DNA String: ")
RNA = DNA.replace('T', 'U')
print("Converted String:", RNA)
