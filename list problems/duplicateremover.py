num = [1, 2, 3, 3, 4, 4, 5]
unique=[]
for i in num:
    if i not in unique:
        unique.append(i)

print("Original list:", num)
print("After removing duplicates:", unique)
