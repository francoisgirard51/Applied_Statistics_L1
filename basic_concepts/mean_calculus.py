# basic mean calculus

import numpy as np
import matplotlib.pyplot as plt

N_points = 20
x = np.random.uniform (0, 100 , N_points)
Mx = np.mean(x)
print(Mx)