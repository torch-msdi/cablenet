import cupy as cp
import numpy as np
import time
import os

os.environ['CUDA_VISIBLE_DEVICES'] = "0"


s = time.time()
x_c = np.ones((800, 800, 800))
e = time.time()
print(e-s)

s = time.time()
x_g = cp.ones((800, 800, 800))
e = time.time()
print(e-s)

s = time.time()
x_c *= 5
x_c *= x_c
x_c += x_c
e = time.time()
print(e-s)

s = time.time()
x_g *= 5
x_g *= x_g
x_g += x_g
e = time.time()
print(e-s)
