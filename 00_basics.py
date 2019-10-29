# Importing numpy
import numpy as np

# Creates an array of 16 numbers with the shape of 3 rows and 5 columns
a = np.arange(15).reshape(3,5)

# Prints the matrix
print(a)

# Prints the shape of matrix
print(a.shape)

# Prints the dimensions of the matrix
print(a.ndim)

# Prints the data type of the matrix
print(a.dtype.name)

# Prints the total number of elements in the array
print(a.size)

# Creating a single axis array (axis being dimension)
b = array([6, 7, 8])
