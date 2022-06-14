#from Geeks for Geeks

#create an empty and a full NumPy array
import numpy as np
#empty
empty = np.empty((3,3),dtype=int)
print(empty)
#full 
full = np.full((3,3),4,dtype=int)
print(full)

# Create a Numpy array filled with all zeros
zeros = np.zeros((3,3),dtype=int)
print(zeros)
# Create a Numpy array filled with all ones
ones = np.ones((3,3),dtype=int)
print(ones)

# Check whether a Numpy array contains a specified row
arr = np.array([[1, 2, 3, 4, 5],
                   [6, 7, 8, 9, 10],
                   [11, 12, 13, 14, 15],
                   [16, 17, 18, 19, 20]
                   ])
a = [6, 7, 8, 9, 10] in arr.tolist()
print(a)


# Remove rows in Numpy array that contains non-numeric values?
n = np.array([[10.5, 22.5, 3.8],
            [41, np.nan, np.nan]])
a = np.isnan(n)
print(a)
b = (n[~a.any(axis=1)])
print(b)

# remove single dimensional entries(changing ndim)
a = np.array([[[1,2,3], [4,5,6]]])
print(a.ndim)  
print(a.shape)
b = np.squeeze(a) 
print(b.ndim)
print(b.shape)


# Find the number of occurrences of a sequence in a NumPy array
arr = np.array([[2, 8, 9, 4], 
                [9, 4, 9, 4],
                [4, 5, 9, 7],
                [2, 9, 4, 3]])
a = repr(arr).count('9, 4') #convert array to string
print(a)


# Find the most frequent value in a NumPy array
arr = np.array([1,2,3,4,5,1,2,1,1,1])
a = np.bincount(arr)
print(a)
max = a.argmax()
time = a.max()
print(f'{max}-{time}times')


# If the array has more than one element having maximum frequency
x = np.array([1, 1, 1, 2, 3, 4, 2, 4, 3, 3, ])
y = np.bincount(x)
maximum = max(y)
print("y - ",y)
print("maximum - ",maximum)

for i in range(len(y)):
    if y[i] == maximum:
        print(i, end=" ")


# Combining a one and a two-dimensional NumPy Array
a = np.array([1, 1, 1, 2,])
b = np.array([[1, 1, 1, 2,]])
for i,j in np.nditer([a,b]):
    print(f'{i}:{j}')


# add a border around a NumPy array
array = np.ones((3,3))
bound = np.pad(array,1,'constant')
print(bound)


# compare two NumPy arrays
a = np.array([1,2,3,4,5])
b = np.array([6,8,3,4,5])
c = a==b
print(c.all())


# get all 2D diagonals of a 3D NumPy array
arr = np.arange(3*4*4).reshape(3,4,4)
print(arr)
d = np.diagonal(arr,axis1=1,axis2=2)
print(d)

# Flatten a Matrix in Python using NumPy
a = np.array([[1,2],[4,5]])
flat = a.flatten()
print(a)
print(flat)

# trim zeros from front and back 
arr = np.array((0, 0, 0, 0, 1, 5, 7, 0, 6, 2, 9, 0, 10, 0, 0))
trim = np.trim_zeros(arr)
print(trim)


# make a NumPy array read-only?
a = np.array([1,2,3,4,5])
a.flags.writeable = False

# count the number of elements along the axis.
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(np.size(arr, 0))
print(np.size(arr, 1))
