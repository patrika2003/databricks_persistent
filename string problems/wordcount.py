sent = input("Enter a sentence: ")
word = ""
count = 0

for char in sent:
    if char != " ":
        word = word + char
    else:
        count = count + 1
        word = ""

if word != "":
    count = count + 1

print(count)
