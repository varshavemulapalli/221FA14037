'''
comparing two DNA sequncesfrom different patients to find mutation  points.
compare two strings of the same length and print positions where the sequences differ
example:
Enter the first Sequence :"AAGCTCGA "
Enter the second sequence:"AACCTAGA"
OUTPUT:[2,5]'''

seq1 = input("Enter the first Sequence: ")
seq2 = input("Enter the second Sequence: ")

mutation_points = []

for i in range(len(seq1)):
    if seq1[i] != seq2[i]:
        mutation_points.append(i)

print("OUTPUT:", mutation_points)
