import numpy as np

print("\n"*2 + "bool_arr:")
bool_arr = np.array([5, 0.001, 1, 0, 'g', None, True, False, ''], dtype=bool)
print(bool_arr)

print("\n"*2 + "np.astype(np.int):")
A = np.array([
    [90, 11, 9, 2, 34, 3, 19, 100,  41],
    [21, 64, 12, 65, 14, 16, 10, 122, 11],
    [10, 5, 12, 15, 14, 16, 10, 12, 12],
    [ 49, 51, 60, 75, 43, 86, 25, 22, 30]
])
B = A < 20
print(B.astype(np.int_))

# Numpy Boolean Array – Logical Operations
# Logical Operations such as: AND, OR, NOT, XOR 
# is also operational on the boolean array with the following syntax method.
a = np.array([True, True, True, False, True, False, True], dtype = bool)
b = np.array([False, True, False, True, True, False, False], dtype = bool)
print("\n"*2 + "np.logical:")

print(np.logical_and(a,b))
print(np.logical_or(a,b))
print(np.logical_not(a))
print(np.logical_xor(a, b))

# Algo interesante
x = np.arange(5)
print(np.logical_xor(x < 1, x > 3))

print("\n"*2 + "1D Boolean indexing:")
# 1D Boolean indexing
A = np.array([1, 2, 3])
B = np.array([True, False, True], dtype = bool)
print(A[B])
# Output: [1, 3] 
 
print("\n"*2 + "2D Boolean indexing:")
# 2D Boolean indexing
A = np.array([
    [4, 3, 7],
    [1, 2, 5]
    ])
B = np.array([
    [True, False, True],
    [False, False, True]
    ], dtype = bool
    )
A[B] = -1
print(A)
# print(A[B])
 
#Output: [4, 7, 5]