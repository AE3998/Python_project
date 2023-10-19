import numpy as np


feat = np.array([1, 2, 3])
N = feat.size
print(N)
padded = np.pad(feat, ((N, N), (0, 0)), mode = 'edge')


