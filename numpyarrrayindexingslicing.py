import numpy as np

# Creating a NumPy array
arr = np.array([1, 2, 3, 4, 5])

# Indexing: Accessing individual elements
print("Element at index 2:", arr[2])

# Slicing: Extracting a subset of elements
subset = arr[1:4]  # Elements at index 1, 2, and 3 (exclusive of 4)
print("Subset using slicing:", subset)

# Modifying elements using indexing
arr[0] = 10
print("Modified array:", arr)

# 2D array indexing and slicing
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Indexing 2D array
element = matrix[1, 2]  # Row 1, Column 2
print("Element at row 1, column 2:", element)

# Slicing 2D array
row_slice = matrix[0:2, :]  # Rows 0 and 1, all columns
print("\nSliced rows 0 and 1:")
print(row_slice)

col_slice = matrix[:, 1]  # All rows, column 1
print("\nSliced column 1:")
print(col_slice)

# Boolean indexing
bool_arr = matrix > 4
print("\nBoolean indexing (elements > 4):")
print(bool_arr)

filtered_arr = matrix[bool_arr]
print("\nFiltered array:")
print(filtered_arr)

# Integer array indexing
indices = np.array([0, 2])
selected_elements = matrix[indices, :]
print("\nSelected elements using integer array indexing:")
print(selected_elements)
