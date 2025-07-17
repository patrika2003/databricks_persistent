import re
text="Hello World"
pattern =r"Hello"

match=re.match(pattern,text)
if match:
  print("Match found at beginning")
else:
  print("No match at beginning")

#match found at beginning of string

#####################################

text="123"
pattern=r"\d+"

if re.fullmatch(pattern,text):
  print("Entire string matches pattern")

#match entire string

##########################################

text="Contact me at john@email.com or jane@example.org"
pattern=r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

emails=re.findall(pattern,text)
print(emails)

####################################

#replace matches
text="The date is 2023-12-25"
pattern=r"(\d{4})-(\d{2})-(\d{2})"
replacement=r"\2/\3/\1"

new_text=re.sub(pattern,replacement,text)
print(new_text)

#####################################
def extract_phone_numbers(text):

  patterns =[
        r"\b\d{3}-\d{3}-\d{4}\b",           # 123-456-7890
        r"\b\(\d{3}\)\s*\d{3}-\d{4}\b",    # (123) 456-7890
        r"\b\d{3}\.\d{3}\.\d{4}\b",        # 123.456.7890
  ]

  phone_numbers=[]
  for pattern in patterns:
    phone_numbers.extend(re.findall(pattern,text))
  return phone_numbers
text="call me at 123-456-7890 or (555) 123-4567"
print(extract_phone_numbers(text))