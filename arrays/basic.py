number=[10,20,30,40]
print(number)

print(number[0])
print(number[-2])

number[1]=50
print(number)

number.append(70)
print(number)
number.insert(0,90)
print(number)
number.remove(30)
print(number)
number.pop()
print(number)
del number[0]  #remove item at index
del number[1:3]  #index 1 and 3 
print(number)
del number #delete entire array

# for num in number:
#   print(num)

