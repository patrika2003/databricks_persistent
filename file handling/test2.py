with open('output.txt','w') as f:
  f.write('Hello world')

lines=['Line1\n','Line2\n','Line3\n']
with open('output.txt','w') as f:
  f.writelines(lines)

with open('output.txt','a') as f:
  f.write('\nAppended text')


