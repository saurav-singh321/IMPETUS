import numpy as np
# Q. Create a 1D array of numbers from 0 to 9
lis = [i for i in range(10)]
print(*lis)

# list comprehension code for addition
o1, o2 = [[[1 for i in range(3)] for j in range(3)] ]*2
print(f"o1 = {o1}")
print(f"o2 = {o2}")
r = [[o1[a][b]+o2[a][b] for a in range(len(o1))] for b in range(len(o2))]
print(f"addition = {r}")

# all odd numbers from arr
a = [i for i in range(10) if i%2==1 ]
print(f"odd = {a}")

# Q. Create a 3×3 numpy array of all True’s
a = [[True for i in range(3)] for j in range(3)]
print(f"True = {a}")

# Q. Replace all odd numbers in arr with -1
a = [-1 if i%2==1 else i for i in range(10)]
print(f"replaced odd with -1 = {a}")

# Q. Get the common items between a and b
a,b = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6]) , np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])
c = [i for i in a if i in b] 
print(f"common = {c}")
