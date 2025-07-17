try:
  result=10/0
except ZeroDivisionError:
  print("Cannot divide by Zero!")


try:
  value=int(input("Enter a number: "))
  result=10/value
  print(result)
except ValueError:
  print("Invalid input!Please enter the no: ")
except ZeroDivisionError:
  print("cannot divide by Zero!")


try:
  pass
except(ValueError, TypeError,ZeroDivisionError) as e:
  print(f"An error occured")


try:
  value=int(input("Enter a number: "))
  result=10/value
  print(result)
except ValueError:
  print("Invalid input!Please enter the no: ")
except ZeroDivisionError:
  print("cannot divide by Zero!")
else:
  print(f"Successfully divided:{value}")

finally:
  print("Project execution completed")