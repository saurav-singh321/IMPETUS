import pickle as pc
data = {1:"saurav",2:"gaurav",3:"aadesh"}

with open('pickle.TXT','wb') as f:
    a = pc.dump(data,f)


with open('pickle.TXT','rb') as f:
    a = pc.load(f)
    print(a)
