rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    print("*" * i)


rows = int(input("Enter number of rows: "))
num = 1
for i in range(1, rows + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

rows = int(input("Enter number of rows: "))

for i in range(rows, 0, -1):
    for j in range(0, i):
        print("* ", end=" ")
    
    print()