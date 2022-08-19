import re
text = """hello i'm saurav singh and i'm 20 years old saurav and i live in Indore
        ha haha
        654.986.5421
        985-683-7830
        827*924*6892
        127--819--6892
        cat 
        mat
        pat
        bat
        Mr. Schafer 
        Mr Smith
        Ms Davis
        Mr. T
        Mrs. Robinson
        sauravsingh@gmail.com
        gaurav.hello@yahoo.in
        aadesh-dangi@education.edu
        """

urls = """https://www.google.com
          http://coreyms.com
          https://youtube.com
          https://www.nasa.gov"""
          
email = re.compile(r'[a-zA-Z0-9_.-]+@[a-zA-Z-]+\.(com|edu|in)')

a = re.compile(r'\d{3}[.-]\d{3}[.-]\d{4}')

b = re.compile(r'[0-9]{3}[.-]\d{3}[.-]\d{4}')

not_b_in_bat = re.compile(r'[^b]at')

names = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-z]\w*')

url = re.compile(r'https?://(www\.)?([a-z]+)(\.(com|gov))')

# getting domain name(group2) and .com(group3)
sub = re.sub(url,r'\2\3', urls)
print(sub)

#it is same as sub but it returns a tuple with the count of number of replacement
sub1 = re.subn(url,r'\2\3', urls)
print(sub1)

#this will give a iterator which have all the matched text
b = re.finditer(url,urls)
for i in b:
    print(i.group(2,3))
 