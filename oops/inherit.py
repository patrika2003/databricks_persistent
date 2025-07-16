class Animal:
  def __init__(self,name):
    self.name=name
    pass
  def species(self):
    return "Hello"
  
class Dog(Animal):
  def sound(self):
    return "woof!"
  
a=Animal("Generic animal")
d=Dog("Buddy")

print(a.name)
print(d.name)
print(d.sound())

print(a.sound())      #error
print(a.species())

print(d.sound())
print(d.species())

