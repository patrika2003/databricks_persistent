set1 = {10, 20, 30, 20, 40}

set1.add(50)
print(set1)
set1.remove(20)            # Error if not present
print(set1)
set1.discard(10)           # No error if not present
print(set1)
set1.pop()                 # Removes a random item
print(set1)
set1.clear()               # Empty the set
print(set1)

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))            # {1, 2, 3, 4, 5}
print(a.intersection(b))     # {3}
print(a.difference(b))       # {1, 2}
print(a.symmetric_difference(b))  # {1, 2, 4, 5}
