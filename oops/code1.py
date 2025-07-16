class Dog:
  species="canine"

  def __init__(self,name,age):
    self.name=name
    self.age=age

dog1=Dog("Max", 5)
dog2=Dog("Buddy", 3)


print(dog1.name)
print(dog2.species)
print(dog2.age)
print(dog2.name)
