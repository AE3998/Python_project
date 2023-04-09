import numpy as np

d = np.arange(18).reshape(2, 3, 3) + 1
print(d)

# np.delete(matrix, obj, axis)

# Quiero eliminar la segunda fila de la matriz 3D
# La fila es el segundo elemento de la matriz, pues
# los indices se cuenta de afuera a adentro. 

# La primer dimension [0] se refiere a la profundidad, 
# luego [1] a la fila y [2] la columna. Es medio rebuscado 
# pensar de esta forma, aunque no esta de todo mal jaj  

# Recordar que se cuenta desde cero: idx = [0, 1, 2, ...]
# La segunda es entonces el indice 1 

print("\n 3D Eliminado la fila 2 = \n", np.delete(d, 1, 1))

# Si la matriz es 2D y quiero eliminar la columna 1, el orden de axis cambia

d = np.arange(9).reshape(3, 3) + 1

print("\n"*2 + "Matriz 2D: \n", d)
print("\n 2D Eliminado la columna 1 = \n", np.delete(d, 0, 1))


# Aplanar la matriz a 1D con axis = None (lo mismo que d.ravel())
# luego eliminar el elemento obj

print("\n"*2 + "Aplanar la matriz y eliminar el 5to elemento",
       np.delete(d, 4, None))

# Puedo eliminar varios objetos usando lista
# Elimino la primera y segunda columna

print("\n"*2 + "Eliminar la primera y segunda columna: \n", 
      np.delete(d, [0, 1], 1))

# Permite tambien trabajar con el formato de slicing
# usando np.s_[0:2] por ejemplo (o incluso [::2] 
# contando desde el inicio con un salto de a 2)

print("\n"*2 + "Eliminar la primera y segunda columna usando np.s_[]: \n", 
      np.delete(d, np.s_[:2], 1))


# No nos permite eliminar varias dimensiones a la vez, 
# por lo que se aplica la funcion varias veces

#Elimino la fila y columna 1

print("\n"*2 + "Eliminar fila y columna 1: \n",
      np.delete(np.delete(d, 0, 1), 0, 0))