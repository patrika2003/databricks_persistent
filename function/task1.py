def get_marks():
  s1 = int(input("Enter marks for Subject 1: "))
  s2 = int(input("Enter marks for Subject 2: "))
  s3 = int(input("Enter marks for Subject 3: "))
  s4 = int(input("Enter marks for Subject 4: "))
  s5 = int(input("Enter marks for Subject 5: "))
  return s1, s2, s3, s4, s5
get_marks()


def calculate_total_marks(marks):
  totalmarks = sum(marks)
  print(totalmarks)
  return totalmarks
total=calculate_total_marks(marks)

def display(marks, total):
  for i in range(len(marks)):
    print("Subject", i + 1, ":", marks[i])
  print("Total Marks:", total)
display(marks, total)

