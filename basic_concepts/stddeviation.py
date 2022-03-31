# COMMENTS: This script calculates the mean and standard deviation of a list of numbers.
# The larger the number of uniform random draws 'N', the more the classified values are
# concentrated around the theoretical standard deviation and therefore the less the
# dispersion of the point estimates. The most favorable condition for having a good
# approximation of the theoretical standard deviation is to have the largest sample
# size (random draw).

import numpy as np
import matplotlib.pyplot as plt

for N in [20,100,1000]:
    sigma_xs = []
    for i in range(50):
        x = np.random.uniform (0, 100 , N)
        sigma_x = np.std(x)
        sigma_xs.append( sigma_x )
    plt.figure()
    plt.hist(sigma_xs,bins=40,range=[15,40])
    plt.show()