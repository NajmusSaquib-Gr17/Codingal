import numpy as np


# Create array of linearly spaced elements between 0 to 9
arr = np.linspace(0, 9, num=10, dtype=int)
print("Original array:", arr)

# Replace all odd numbers with -1 without modifying the original array
arr_odd_replaced = np.where(arr % 2 != 0, -1, arr)
print("Odd numbers replaced with -1:", arr_odd_replaced)

# Convert into 2D array with two rows
arr_2d = arr.reshape(2, -1)
print("2D array:\n", arr_2d)

# Sum of all even numbers
sum_even = np.sum(arr[arr % 2 == 0])
print("Sum of even numbers:", sum_even)



# Array Creation

zeros_arr = np.zeros(5)
ones_arr = np.ones((2, 3))
full_arr = np.full((2, 3), 7)
arange_arr = np.arange(0, 10, 2)
eye_arr = np.eye(3)
rand_arr = np.random.rand(3, 3)
rand_int_arr = np.random.randint(0, 10, size=(3, 3))

print("\nZeros array:", zeros_arr)
print("Ones array:\n", ones_arr)
print("Full array with 7s:\n", full_arr)
print("arange array:", arange_arr)
print("Identity matrix:\n", eye_arr)
print("Random float array:\n", rand_arr)
print("Random int array:\n", rand_int_arr)



# Indexing, Slicing, Boolean Masking

print("\nFirst element:", arr[0])
print("Last element:", arr[-1])
print("First three elements:", arr[:3])
print("Elements from index 3 to 7:", arr[3:8])
print("Even numbers only:", arr[arr % 2 == 0])
print("Odd numbers only:", arr[arr % 2 != 0])



# Mathematical Operations

print("\nArray + 5:", arr + 5)
print("Array * 2:", arr * 2)
print("Array squared:", np.square(arr))
print("Square root:", np.sqrt(arr))
print("Sine values:", np.sin(arr))
print("Exponential:", np.exp(arr))
print("Logarithm:", np.log(arr + 1))  # +1 to avoid log(0)



# Aggregation & Statistics

print("\nSum of all elements:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Standard deviation:", np.std(arr))
print("Variance:", np.var(arr))
print("Min value:", np.min(arr))
print("Max value:", np.max(arr))
print("Index of min:", np.argmin(arr))
print("Index of max:", np.argmax(arr))



# Reshaping, Stacking, Splitting

reshaped = np.arange(1, 13).reshape(3, 4)
print("\nReshaped array (3x4):\n", reshaped)

vstacked = np.vstack([arr, arr])
hstacked = np.hstack([arr, arr])
print("Vertical stack:\n", vstacked)
print("Horizontal stack:\n", hstacked)

split_arrays = np.array_split(arr, 2)
print("Split arrays:", split_arrays)



# Sorting & Searching

unsorted_arr = np.array([3, 1, 4, 1, 5, 9, 2])
print("\nSorted array:", np.sort(unsorted_arr))
print("Indices that would sort array:", np.argsort(unsorted_arr))
print("Where arr == 5:", np.where(unsorted_arr == 5))



# Broadcasting Example

broadcasted = arr_2d + np.array([10, 20, 30, 40, 50])
print("\nBroadcasting result:\n", broadcasted)



# Linear Algebra

mat1 = np.array([[1, 2], [3, 4]])
mat2 = np.array([[5, 6], [7, 8]])

print("\nMatrix multiplication:\n", np.dot(mat1, mat2))
print("Transpose:\n", mat1.T)
print("Determinant:", np.linalg.det(mat1))
print("Inverse:\n", np.linalg.inv(mat1))



# Random Operations

print("\nRandom choice:", np.random.choice(arr))
print("Shuffle array:", np.random.permutation(arr))


# Set Operations

arr_a = np.array([1, 2, 3, 4])
arr_b = np.array([3, 4, 5, 6])

print("\nUnique elements in arr_a:", np.unique(arr_a))
print("Union:", np.union1d(arr_a, arr_b))
print("Intersection:", np.intersect1d(arr_a, arr_b))
print("Set difference:", np.setdiff1d(arr_a, arr_b))
