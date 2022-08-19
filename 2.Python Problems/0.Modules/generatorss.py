#creating generator for 1st iterator problems
def gen(start,end):
    while(start<=end):
        yield start
        start+=1
    
g = gen(1,5)
for i in g:
    print(i)


# # creating generator for second iterator
def gen(sentence):
    sen = sentence.split(' ')
    for i in sen:
        yield i

a = gen("This is a test sentence")
for i in a:
    print(i)  

# #fibonacci series 
print("fibonacci series")
limit = int(input("Enter Number: "))
def fibbo(limit):
    a,b = 0,1
    while(a<=limit):
        yield a
        a,b = b,a+b

a = fibbo(limit)
for i in a:
    print(i )
    