import numpy as np

# 1D array
arr_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:")
print(arr_1d)

# 2D array (matrix)
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\n2D Array:")
print(arr_2d)


# Array of zeros
zeros_arr = np.zeros((3, 4))
print("Array of Zeros:")
print(zeros_arr)

# Array of ones
ones_arr = np.ones((2, 3))
print("\nArray of Ones:")
print(ones_arr)

# Array with constant value
constant_arr = np.full((3, 3), 7)
print("\nArray with Constant Value:")
print(constant_arr)


# Array with a range of values
range_arr = np.arange(1, 10, 2)  # Start, stop (exclusive), step
print("Array with Range of Values:")
print(range_arr)

# Array with evenly spaced values
linspace_arr = np.linspace(0, 1, 5)  # Start, stop, number of values
print("\nArray with Evenly Spaced Values:")
print(linspace_arr)

# Identity matrix
identity_matrix = np.eye(3)
print("Identity Matrix:")
print(identity_matrix)