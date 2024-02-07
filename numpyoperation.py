import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

addition_result = np.add(arr1, arr2)
subtraction_result = np.subtract(arr1, arr2)
multiplication_result = np.multiply(arr1, arr2)
division_result = np.divide(arr1, arr2)
exponentiation_result = np.power(arr1, arr2)

arr = np.array([1, 2, 3, 4, 5])
sum_result = np.sum(arr)
mean_result = np.mean(arr)
max_result = np.max(arr)
min_result = np.min(arr)
std_dev_result = np.std(arr)
variance_result = np.var(arr)

arr1 = np.array([1, 2, 3])
arr2 = np.array([2, 2, 2])

greater_than_result = np.greater(arr1, arr2)
less_than_result = np.less(arr1, arr2)
equal_to_result = np.equal(arr1, arr2)
logical_and_result = np.logical_and(greater_than_result, less_than_result)

arr = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5, 3])

sorted_arr = np.sort(arr)
argsort_result = np.argsort(arr)

matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

dot_product_result = np.dot(matrix1, matrix2)
matmul_result = np.matmul(matrix1, matrix2)
inverse_matrix = np.linalg.inv(matrix1)
eigenvalues, eigenvectors = np.linalg.eig(matrix1)