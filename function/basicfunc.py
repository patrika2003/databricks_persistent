def greet():
  print("hello,World!!")
greet()

#with parameters
def greet(name):
  print("hii", name)
greet("patrika")

#with return
def multiplication(a,b):
  return a*b
result=multiplication(5,7)
print("multiplication:", result)

#default parameter
def greet(name="guest"):
  print("hello,", name)
greet()
greet("patrika")

#multiple return value

#kwargs
def info(**details):
  for key,value in details.items():
    print(key,":",value)
info(name="alice", age=25, city="new york")