"""
There are several ways to create arrays.

For example, you can create an array from a regular Python list or tuple
using the array function. The type of the resulting array is deduced from
the type of the elements in the sequences.
"""

import numpy as np

a = np.array([2, 3, 4])
print("This is a numpy array:\n", a)
print("The data type of the numpy array is", a.dtype)

b = np.array([2.36, 4.58, 4.81])
print("This is another numpy array", b)
print("The data type of this array is", b.dtype)

"""
array transforms sequences of sequences into two-dimensional arrays,
sequences of sequences of sequences into three-dimensional arrays, and so on.
"""

# Both ways are fine
# c = np.array([(1.5, 2, 6), (4, 5, 6)])
c = np.array([[1.5, 2, 6], [4, 5, 6]])
print("This is a two dimensional array", c)

"""
The type of the array can also be explicitly specified at creation time
"""
d = np.array([[1, 2],[3, 4]], dtype = complex)
print("This is an array of complex data type:\n", d)

"""
Often, the elements of an array are originally unknown, but its size is known.
Hence, NumPy offers several functions to create arrays with initial placeholder
content. These minimize the necessity of growing arrays, an expensive operation.

The function zeros creates an array full of zeros, the function ones creates
an array full of ones, and the function empty creates an array whose initial
content is random and depends on the state of the memory. By default, the dtype
of the created array is float64.
"""
e = np.zeros((3,4))
print("This is an array of zeros:\n", e)

# Creates two arrays of three rows and four columns
f = np.ones((2, 3, 4), dtype = np.int16)
print("This is an array of ones:\n", f)

g = np.empty((2, 3))
print("This is an empty array:\n", g)

"""
To create sequences of numbers, NumPy provides a function analogous to range
that returns arrays instead of lists.
"""

h = np.arange(10,30,5)
print("The array range from 10 to 30 is:\n", h)

i = np.arange(0, 2, 0.3)
print("The array range from 0 to 2 is:\n", i)

"""
When arange is used with floating point arguments, it is generally not possible
to predict the number of elements obtained, due to the finite floating point
precision. For this reason, it is usually better to use the function linspace that
receives as an argument the number of elements that we want, instead of the step:
"""

# This prints 9 numbers from 0 to 2
j = np.linspace(0, 2, 9)
print("This array is created by using linspace:\n", j)

from numpy import pi

x = np.linspace(0, 2*pi, 100)
k = np.sin(x)
print(k)
