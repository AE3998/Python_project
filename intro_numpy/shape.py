import numpy as np

# ========================[size(d), d']==========================


"""
d = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print("shape", d.shape)

## Transpuesta
dt = d.T
print(dt)
"""

# ========================扁平化 [nD -> 1D]==========================
"""
d = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
# Funcion ravel devuelve un vector con todos los elementos de 
# la matriz
print(d.ravel())

"""
# ======================== reshape(m, n)==========================


d = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
# la dimension debe coincidir con la cantidad total de elementos
print(d.reshape(3, 2))
print(d.reshape(6, 1))

# Uso frecuente de reshape

d = np.ones(15).reshape(3,5)
print(d)

