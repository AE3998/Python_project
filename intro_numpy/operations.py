import numpy as np


# ===========逐一元素運算 d1 [+, -, *, /, >, ==, <=, etc] d2 ===========
"""
d1 = np.array([1, 2, 3])
d2 = np.array([4, 5, 6])
print(d1 >= 2)
"""

# ============================矩陣運算==============================
"""
d1 = np.array([1,2,3])
d2 = np.array([
    [1, 2],
    [3, 4], 
    [5, 6]
])

# Producto punto
res1 = d1.dot(d2)
res2 = d1@d2
print("\nProducto usando d1.dot(d2) ", res1)
print("\n Producto usando d1@d2 ", res2)

# Outer product (producto cruz)
print("\n Producto outer", np.outer(d1, d2))
"""
# ============================統計運算==============================

d = np.array([
    [1, 2, 3],
    [4, 1, 6]
])
print(d.sum())              # Sumar todo
print(d.sum(axis = 0))         # Sumar filas [1+4]
print(d.sum(axis = 1))         # Sumar columnas [1+2+3] 

print("maxima: ", d.max(axis=0))             # maximo  
print(d.min())             # minimo
print(d.cumsum())          # 逐值累加
print(d.mean())             # 平均數
print(d.std())              # 標準差


