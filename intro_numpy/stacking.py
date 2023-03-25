import numpy as np

# 將數個多微陣列合併成一個, por su puesto que verticalmente o 
# horizontalmente, la dimension debe ser lo mismo

ar1 = np.array([
    [3, 4]
]) # 1x2

ar2 = np.array([
    [5, 6]
]) # 1x2
ar3 = np.array([
    [7]
])
# 合併第一個維度 vstack (vertical stack (?)) 
res1 = np.vstack( (ar1, ar2) )
print(res1)

# [[3, 4],[5, 6]] 2x2 = 1+1x2

# 合併第二個維度 hstack (horizontal stack (?))
res2 = np.hstack( (ar1, ar2) )
print(res2)
# [[3, 4, 5, 6]] 1x4 = 1x2+2

# Test

# ERROR
# res = np.vstack((ar1, ar2, ar3))
# print(res)

# CORRECTO
res = np.hstack((ar1, ar2, ar3))
print(res)

idx = res1 == 5
print(res1[idx])


