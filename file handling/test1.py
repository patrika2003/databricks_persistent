with open('file.txt','r') as f:
  content=f.read()

with open('file.txt','r') as f:
  for line in f:
    print(line.strip())

with open('file.txt','r') as f:
  lines=f.readlines()

with open('file.txt','r') as f:
  first_line=f.readline()

