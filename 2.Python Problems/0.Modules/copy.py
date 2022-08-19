import copy
import copy
a = [[1,2,3,4],[4,5,6,7]]
b = a.copy()

a[1][0]= 25

print(a)
print(b)

print(id(a))
print(id(b),"\n")
print(id(a[0]))
print(id(b[0]))


a = [[1,2,3,4],[4,5,6,7]]
b = copy.deepcopy(a)

a[1][0]= 25

print(a)
print(b)

print(id(a))
print(id(b),"\n")
print(id(a[0]))
print(id(b[0]))



