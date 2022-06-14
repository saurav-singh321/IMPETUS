import numpy as np

#create an empty and a full NumPy array
#empty
empty = [[[]for i in range(3)]for j in range(3)]
print(f"empty = {empty}")
#full 
full = [[4 for i in range(3)]for j in range(3)]
print(f"full = {full}")

# Create a Numpy array filled with all zeros
zeros = [[0 for i in range(3)]for j in range(3)]
print(f"zeroes = {zeros}")

# Create a Numpy array filled with all ones
ones = [[1 for i in range(3)]for j in range(3)]
print(f"ones = {ones}")

# Check whether a Numpy array contains a specified row
# ask
arr = np.array([[1, 2, 3, 4, 5],
                   [6, 7, 8, 9, 10],
                   [11, 12, 13, 14, 15],
                   [16, 17, 18, 19, 20]
                   ])
a = [6, 7, 8, 9, 10] in arr
# print(a)


# # Remove rows in Numpy array that contains non-numeric values?
#  any functions return true if any item in an iterable is true
n = np.array([[10.5, 22.5, 3.8],
            [41.0, np.nan, np.nan]])
c = [n[~(np.isnan(n)).any(axis=1)] for i in range(1)]
print(f"Removed non numeric rows = {c}")

# Find the most frequent value in a NumPy array
arr = np.array([1,2,3,4,5,1,2,1,1,1])
a = np.bincount(arr)
b = [[f"{a.argmax()}-{a.max()} times"] for i in range(1)]
print(*b)

# If the array has more than one element having maximum frequency
x = np.array([1, 1, 1, 2, 3, 4, 2, 4, 3, 3, ])
print("x = ", x)
y = np.bincount(x)
maximum = max(y)
print(f"y - {y} \nmaximum - {maximum}")
p = [i for i in range(len(y)) if y[i]== maximum]
print(p)

# Combining a one and a two-dimensional NumPy Array
a,b = [np.array([1, 1, 1, 2,])]*2
c = [f'{i}:{j}' for i,j in np.nditer([a,b])]
print(c)

 