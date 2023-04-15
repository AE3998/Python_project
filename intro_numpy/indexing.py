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

"""
## Prueba personal, extraer submatriz

d = (np.arange(9)+1).reshape(3,3)
print(d)

# quiero llegar la funcion d([3,1], [3, 1]) del Octave
# El famoso sub_matriz
idx = np.array([2, 0])

newD = (d[:, idx])[idx, :]
newD += 1
print("\n",newD)
# Como no hace por referencia, no afecta a la matriz original
print("newD += 1 = \n",d)

# Este tampoco afecta, ya que es una copia de la original
d[:, idx][idx, :] += 10
print("d[:, idx][idx, :] = \n",d)

# otro intento, idx.T es igual a idx   :(
print(idx.T)
print(idx)
print(idx.T == idx) # [True, true]

# Es casi obligatorio hacer reshape para invertir de vector fila a columna
idxT = idx.reshape(idx.size, 1)
print(idxT)

# ASI ES! ESTO ES LO QUE QUIERO LLEGAR 
print("d[idxT, idx] = ", d[idxT, idx])

# NO FUNCIONA
print("d[idx.T, idx] = ", d[idx.T, idx])
# print("d([[2], [0]], [2, 0]]) = ", d[[[2], [0]], [2, 0]])
"""



# Alternativa de suma de sub_matriz, pero fea
"""
d = (np.arange(9)+1).reshape(3,3)
print("d = \n",d)

idx = np.array([2, 0])

newD = (d[:, idx])[idx, :]
print("newD = \n",newD)



for i in range(idx.size):
    d[idx[i], idx] += newD[i, :]

print("ciclo for = \n",d)
"""

# Ejemplos de Numpy, saltos
"""
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[::2])
print(arr[1:5:2])
print(arr[-3:-1])
"""
# ======================== d[..., 0:2]  ==========================

# Cuando uso ..., quiere decir "Dame todo".
# Se coloca a la derecha o la izquierda del corchete,
# los elementos te lo representa por fila.
"""
d = np.array([
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [7, 8, 9],
        [10,11,12]
    ]
])

print(d[..., 2])
# [[ 3  6] 
#  [ 9 12]]


"""


# Tutorial https://numpy.org/doc/stable/user/basics.indexing.html

# Forma aun mas rapido para acceder a submatriz
d = np.arange(15).reshape(3, 5) + 1
d.shape = (5, 3) # Otra forma de hacer reshape
# d = np.arange(16).reshape(4, 4) + 1
print(d, "\n"*2)
# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]
#  [13 14 15]] 


# # Extraer una parte de la matriz
print(d[np.ix_([0, 4, 3], [0, 2])])
# [[ 1  3]
#  [13 15]
#  [10 12]]

# # Sumar 1 a una parte de la matriz
# d[np.ix_([0, 3], [0, 3, 1])] += 1
# print(d)

mask = np.array([0, 1])
# idx = np.array([1, 2])
print(~mask, "\n"*2) # ~mask = [-1, -2], contando desde atras
print("\n d[~mask] = \n" , d[~mask])
#  [[13 14 15]
#  [10 11 12]]

# print("\nd[not(mask.any)] =\n", d[not(mask.any)])
print(not(mask.any))
#False


# New axis
x = np.arange(5)
print("\n x[:, np.newaxis] = \n", x[:, np.newaxis])
# [[0]
#  [1]
#  [2]
#  [3]
#  [4]]
print("\n x[:, np.newaxis, np.newaxis] = \n", x[:, np.newaxis, np.newaxis])
# [[[0]]
#  [[1]]
#  [[2]]
#  [[3]]
#  [[4]]]

d = np.array([
   [[1, 2],
    [3, 4]],
   [[5, 6],
    [7, 8]],
])
print("\n"*2 + "d[0, 1, 1] = ", d[0, 1, 1])

d = np.arange(5)
print("\n"*2 + "d = ", d)


x = np.array([[0, 1], [1, 1], [2, 2]])
rowsum = x.sum(-1)
print(rowsum)
x[rowsum <= 2, :]

# Truco: Puedo usar x[:, np.newaxis] en vez de usar reshape, nunca pense eso
x = np.arange(16).reshape(4, 4) # o tambien x.shape = (4, 4), es lo mismo
idx = np.array([0, 3])
idxT = idx[:, np.newaxis]

print(x[idxT, idx])
# Por su puesto, puedo usar tranquilamente el x[np.ix_(rows, columns)]
# donde las entradas pueden ser integer o boolean; obviamente coincidiendo
# el tamano de la matriz. Una excepcion, si el vector fila/columna es booleana
# y el tamano es menor de lo que se le corresponde, se lo rellena con false 
# al resto de los espacios
print("x[np.ix_([True, False, True], idx)] = ") 
print(x[np.ix_([True, False, True], idx)])


# Use a 2-D boolean array of shape (2, 3) with four True 
# elements to select rows from a 3-D array of shape (2, 3, 5) 
# results in a 2-D result of shape (4, 5):
x = np.arange(30).reshape(2, 3, 5)
# array([[[ 0,  1,  2,  3,  4],
#         [ 5,  6,  7,  8,  9],
#         [10, 11, 12, 13, 14]],
#       [[15, 16, 17, 18, 19],
#         [20, 21, 22, 23, 24],
#         [25, 26, 27, 28, 29]]])
b = np.array([[True, True, False], [True, True, True]])
print(x[b])
# Esto equivale a decir: "De primer dimension quiero el 1ro y 2do, de 
# segunda dimension quiero la 1ro, 2do y 3ro elemento".


