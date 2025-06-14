'''calculate the GC content as a percentage
classifies the sequ. as:
"High GC " if GC% > 60
"Moderate GC "if GC% is between 40 and 60
"Low GC" if GC% =< 40'''
sequence = input("Enter the DNA sequence: ")
GC_count = 0
for i in sequence:
    if i == 'G' or i == 'C':
        GC_count += 1
GC_percent = (GC_count / len(sequence)) * 100
print("GC Content: ", GC_percent, "%")
if GC_percent > 60:
    print(" High GC")
elif GC_percent >= 40:
    print("Moderate GC")
else:
    print(" Low GC")
