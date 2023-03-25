import numpy as np

# Como consejo para entender el problema de dimensiones
# es "adecuado" pensar simepre que los ultimos 2 indices 
# se corresponde a la fila y columna. Los indices anteriores
# de estos dos son para dimensiones mayores. 

""" 
Por ejemplo:
    a = np.ones([2, 3, 1]) 

Se puede interpretar como 2 en profundo, 3 filas y 1 columna
Asi sucesivamente para las dimensiones mayores.
Por ejemplo:
    a = np.ones([3, 2, 3, 1])

Se puede interpretar como 3 en 4D, 2 en profundo, 3 filas y 1 columna

[[[[1.]
   [1.]
   [1.]]

  [[1.]
   [1.]
   [1.]]]


 [[[1.]
   [1.]
   [1.]]

  [[1.]
   [1.]
   [1.]]]


 [[[1.]
   [1.]
   [1.]]

  [[1.]
   [1.]
   [1.]]]]

"""

## def multiply(a,  b):
##     return a*b       


# a = np.array([1,2,3])
# b = np.array([1,2,3])
# res = multiply(a, b)
# print(res)

# 1D array 
# a = np.empty(4)
# print(a)
# a = np.ones(4)
# print(a)
# a = np.zeros(3)
# print(a)
# a = np.arange(4)
# print(a)

# ===========================2D array=============================

"""
a = np.array([
    np.zeros(3),
    np.ones(3),
    np.arange(3)
])
print(a)


a = np.ones([4, 4])
print(a)
 """
# Hay error, no reconoce esta funcion 
#   a = np.arange([3,3])
# ===========================3D array=============================
""" 
a = np.array([
    [
        [1, 2],
        [3, 4], 
        [5, 6]
    ], [
        [7, 8], 
        [9, 10],
        [11, 12]    
    ]
])
print(a)

a = np.ones([2, 3, 2])
print(a)
"""
# ===========================3D array=============================

a = np.ones([3, 2, 3, 1])
print(a)
