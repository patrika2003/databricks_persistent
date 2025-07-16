class Parent():

  def show(self):
    print("Inside parent")

class Child(Parent):
  def show(self):
    # super().show()
    print("Inside child")

obj=Child() #child
obj.show()

obj1=Parent()  #parent
obj1.show()