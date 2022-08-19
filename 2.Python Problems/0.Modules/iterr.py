list1 = ['saurav','hitakshi']
it = iter(list1)
print(it)
print(next(it))
print(next(it))

# creating our iterator

class MyRandom:
    def __init__(self,start,end):
        self.start = start
        self.end = end
    
    def __iter__(self):
        #it will convert the class object in iterable
        return self 

    def __next__(self):
        if self.start < self.end:
            current = self.start
            self.start += 1
            return current
        else:
            raise StopIteration

m = MyRandom(1,5)
for i in m:
    print(i)

# creating our iterator
class Sentence:
    def __init__(self,sentence):
        self.sentence = sentence
        self.length = 0
        self.current = self.sentence.split(' ')

    def __iter__(self):
        return self

    def __next__(self):
        leng = self.length

        if leng>=len(self.current):
            raise StopIteration
        else:
            self.length+=1
            return self.current[leng]
            
s = Sentence('This is a test sentence')
for i in s:
    print(i)



