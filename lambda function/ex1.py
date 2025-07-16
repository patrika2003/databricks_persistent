add = lambda a, b: a + b
print(add(3, 7))  # Output: 10


from functools import reduce
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)
print("Total sum:", total)

nums = [5, 10, 15]
plus_ten = list(map(lambda n: n + 10, nums))
print("After adding 10:", plus_ten)

