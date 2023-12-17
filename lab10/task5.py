# Task 5
# Create 2D (4,4) array with random numbers from 0 to 100 and perform the following:
# 1-	Print the array data type.
# 2-	Make copy of the array, sort the copy and check if array owns its data.
# 3-	Print all even index array elements (index , value)
# 4-	Convert the array into a 1D array.
# 5-	Find the highest 5 values in 1D array.
# 6-	Convert the array to text array.


import numpy as np

array = np.random.randint(0, 100, (4, 4))
print(array)
print('Data type:', array.dtype)
array_copy = array.copy()
array_copy.sort()
print(array_copy)
print("base of array_copy:", array_copy.base)

for index, value in np.ndenumerate(array):
    if index[0] % 2 == 0 and index[1] % 2 == 0:
        print(index, value)

# 2 ways to convert to 1D array
one_d_array = array.flatten()
one_d_array_v2 = array.reshape(-1)
print(one_d_array)

# find highest 5 values
highest_5_values = np.sort(one_d_array)[-5:]
print(highest_5_values)

# convert one_d_array to text array
text_array = one_d_array.astype(str)
print(text_array)