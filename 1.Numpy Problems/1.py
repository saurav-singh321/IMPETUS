import numpy as np
# Q. Create a 1D array of numbers from 0 to 9
a = np.arange(0, 10)
print(a)
# python
lis = []
for i in range(10):
    lis.append(i)
print(*lis, sep=' ')


# Q. Create a 3×3 numpy array of all True’s
a = np.full((3, 3), True, bool)
print(a)
# python
o = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(True)
    o.append(row)
print(o)


#  Q. matrix addition
a = np.full((3, 3), 1, int)
b = np.full((3, 3), 1, int)
print(a)
print(b)
print(a+b)
# python
o1 = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(1)
    o1.append(row)
print(o1)
o2 = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(1)
    o2.append(row)
print(o2)
o = []
for k in range(len(o1)):
    row = []
    for l in range(len(o2)):
        c = f"{o1[k][l]+o2[k][l]}"
        row.append(c)
    o.append(row)
print(o)


#  Q. Extract all odd numbers from arr
arr = np.arange(0, 10)
print(arr)
print(arr[arr % 2 == 1])
# python
lis = []
for i in range(10):
    if i % 2 == 1:
        lis.append(i)
print(*lis, sep=' ')


# Q. Replace all odd numbers in arr with -1
arr = np.arange(0, 10)
out = np.where(arr % 2 == 1, -1, arr)
print(out)
print(arr)
# python
lis = []
for i in range(10):
    lis.append(i)
print(lis)
for j in range(len(lis)):
    if lis[j] % 2 == 1:
        lis[j] = -1
print(lis)

# Q. Convert a 1D array to a 2D array with 2 rows
arr = np.arange(0, 10)
print(arr)
arr = arr.reshape(2, -1)
print(arr)
# python

# Q. Stack arrays a and b vertically
a = np.arange(10).reshape(2, -1)
b = np.repeat(1, 10).reshape(2, -1)
c = np.vstack((a, b))
print(c)

# Q. Create the following pattern without hardcoding. Use only numpy functions and the below input array a.
a = np.array([1, 2, 3])
b = np.r_[np.repeat(a, 3), np.tile(a, 3)]
print(b)

# Q. Get the common items between a and b
a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])
c = np.intersect1d(a, b)
print(c)


# Q. Swap columns 1 and 2 in the array arr.
arr = np.arange(9).reshape(3, 3)
print(arr)
arr = arr[:, [0, 2, 1]]
print(arr)

# Q. Reverse the columns of a 2D array arr.
arr = np.arange(9).reshape(3, 3)
print(arr)
arr = arr[:, ::-1]
print(arr)

# Q. set decimal places upto 3
rand_arr = np.random.random((5, 3))
np.set_printoptions(precision=3)
print(rand_arr)

# Q. Limit the number of items printed in python numpy array a to a maximum of 6 elements.
a = np.arange(15)
np.set_printoptions(threshold=6)
print(a)





