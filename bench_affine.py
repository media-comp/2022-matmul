from affine import f

import numpy as np
import time

A = np.array([
    [1, 3],
    [5, 8]
])

B = np.array([
    [4, 2],
    [1, 4]
])

X = np.array([
    [2, 0],
    [1, -1]
])

gt = np.array([
    [9, -1],
    [19, -4]
])

t0 = time.time()
C = f(A, B, X)
elapsed = time.time() - t0

print(f"{elapsed * 1000} msec")

err = np.sum((C - gt) ** 2)

print(f"Error: {err}")
