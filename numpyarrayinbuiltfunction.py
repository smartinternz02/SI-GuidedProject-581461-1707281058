import numpy as np

arr = np.array([1, 2, 3, 4, 5])
zeros_arr = np.zeros((3, 4))
ones_arr = np.ones((2, 3))
range_arr = np.arange(1, 10, 2)
linspace_arr = np.linspace(0, 1, 5)

arr = np.array([[1, 2, 3], [4, 5, 6]])
reshaped_arr = np.reshape(arr, (3, 2))
concatenated_arr = np.concatenate((arr, reshaped_arr), axis=1)
sub_arrays = np.split(concatenated_arr, [2], axis=1)


arr = np.array([[1, 2, 3], [4, 5, 6]])
sum_value = np.sum(arr)
mean_value = np.mean(arr)
max_value = np.max(arr)
min_value = np.min(arr)

arr = np.array([1, 2, 3, 4, 5])
std_dev = np.std(arr)
variance = np.var(arr)

matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
dot_product = np.dot(matrix1, matrix2)
inverse_matrix = np.linalg.inv(matrix1)