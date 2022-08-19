import re
#1. Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9)
text = "ABCDEFabcdef123450"
text1 = "*&%@#!}{"

pas = re.compile(r'[a-zA-Z0-9]')
matching = re.finditer(pas,text1)

for i in matching:
    print(i)

# 2. Write a Python program that matches a string that has an a followed by zero or more b's. Go to the editor
text = """abc 
        a
        ab
        abb"""

pas = re.compile(r'a(b*)')
matching = re.finditer(pas,text)
for i in matching:
    print(i)