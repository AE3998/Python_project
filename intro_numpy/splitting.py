import numpy as np

# 將一個多維陣列切割成很多個 

d = np.array([
    [1,2,3,4],
    [5,6,7,8]
]) #2x4

# 根據第一個維度切割
res1 = np.vsplit(d, 2)
print(res1)
# [[1,2,3,4]] 1x4
# [[5,6,7,8]] 1x4

# En res1 se almacena un arreglo de arreglos
aux1 = res1[0]
aux2 = res1[1]
print(aux1)

# 根據第二個維度切割
res1 = np.hsplit(d, 2)
print(res1)
# [[1,2],[5,6]] 2x2
# [[3,4],[7,8]] 2x2

"""
# Fuera del tema, test para convertir un vector a un arreglo de numpy
idx = [1, 2, 3]
print(np.array(idx))
"""