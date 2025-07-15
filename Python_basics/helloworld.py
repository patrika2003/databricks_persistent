print("Hello, World!")
'''this is multi line comment'''
num_str="123"
num_int=int(num_str)
print(num_int)

a=5
b=9.5
sum=a+b
print(sum)

my_set = {1, 2, 3, 3, 4}
print(my_set)          
my_set.add(1.5)          
print(my_set)  

my_set = {1, 2, 3}
immutable_set = frozenset(my_set)

print(immutable_set)     

# Try to add element → Will raise an error
immutable_set.add(4)     # AttributeError: 'frozenset' object has no attribute 'add'
