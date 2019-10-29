"""
When you print an array, NumPy displays it in a similar way to nested lists,
but with the following layout:

    ~ the last axis is printed from left to right,

    ~ the second-to-last is printed from top to bottom,

    ~ the rest are also printed from top to bottom, with each slice separated
    from the next by an empty line.

One-dimensional arrays are then printed as rows, bidimensionals as matrices
and tridimensionals as lists of matrices.
"""
import numpy as np

# One dimensional array
a = np.arange(6)
print("One dimensional array is printed as row:\n", a)

# Two dimensional array
b = np.arange(12).reshape(4, 3)
print("Bidirectional array is printed as matrix:\n", b)

# Three dimensional array
c = np.arange(24).reshape(2, 3, 4)
print("Tridimensional array is printed as list of matrices:\n", c)

"""
If an array is too large to be printed, NumPy automatically skips the central
part of the array and only prints the corners:
"""

d = np.arange(10000)
print(d)

e = d.reshape(100, 100)
print(e)

"""
To disable this behaviour and force NumPy to print the entire array, you can
change the printing options using set_printoptions.
"""
# import sys
# np.set_printoptions(threshold=sys.maxsize)
