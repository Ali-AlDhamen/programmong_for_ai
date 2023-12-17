# Task 4
# Write a program to remove the negative values in a NumPy array with 0.
# Sample Output:
# Original array:
# [-1 -4  0  2  3  4  5 -6]
# Replace the negative values of the said array with 0:
# [0 0 0 2 3 4 5 0]


import numpy as np

array = np.array([-1, -4, 0, 2, 3, 4, 5, -6])
print('Original array:')
print(array)
array[array < 0] = 0
print('Replace the negative values of the said array with 0:')
print(array)
