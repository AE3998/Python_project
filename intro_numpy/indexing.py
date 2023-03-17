import numpy as np

# ======================== index 1D ==========================
"""
d = np.arange(5)
# 3
print(d[3])
# ======================== index nD==========================
d = np.arange(18).reshape(2, 3, 3)
print(d)
# Practica de sacar el numero que quiero
# 14
print(d[1,1,2])
"""
# ======================== slicing  ==========================

"""
d = np.arange(6)+1
print(d)
print("d[2:] = ", d[2:])            
print("d[:3] = ", d[:3])
print("d[:] = ", d[:])

"""
# ======================== slicing nD  ==========================
"""
d = (np.arange(6)+1).reshape(2, 3)
print(d)
newD = d[[1, 0], [2, 0]] ## Lo que hizo fue extraer d(1,2) y d(0, 0)
print("\n",newD)

newD = d[[0, 1], [2, 0]] ## Lo mismo sucede aqui, d(0, 2), d(1, 0)
print("\n",newD)
"""


## Prueba personal
d = (np.arange(9)+1).reshape(3,3)
print(d)

# quiero llegar la funcion d([3,1], [3, 1]) del Octave
idx = np.array([2, 0])
# print([idx, [idx, idx]])

# newD = d[idx, [idx, idx]] 

newD = d[[2, 0], [[2, 0], [2, 0]]] 

print("\n",newD)

"""
# Ejemplos de Numpy
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[::2])
print(arr[1:5:2])
print(arr[-3:-1])
"""
# ======================== d[..., 0:2]  ==========================

