import json

with open('data.json','r') as f:
  data=json.load(f)

data={'name':'Alice','age':30}
with open('output.json','w') as f:
  json.dump(data,f,indent=2)


with open('download.jpg','rb') as f:
  binary_data=f.read()

with open('copy.jpg','wb') as f:
  f.write(binary_data)