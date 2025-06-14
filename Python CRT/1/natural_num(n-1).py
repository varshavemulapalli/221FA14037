'''12.to print natural numbers from n to 1'''

n = int(input("Enter the value of n: "))
print(f"Natural numbers from {n} to 1:")
for i in range(n, 0, -1):
    print(i, end=' ')
