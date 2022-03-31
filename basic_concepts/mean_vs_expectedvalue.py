# COMMENTS: This script calculates the mean and expected value of a list of numbers.
# The distribution of the experimental means roughly estimated the expected value
# of the uniform law between 0 and 100. Indeed, the expected value gives an average
# of probability distribution while the experimental average represents only an
# average value of a sample of values.

import numpy as np
import matplotlib.pyplot as plt

N = 20
Mxs = []
for i in range(50):
    x = np.random.uniform (0, 100 , N)
    Mx = np.mean(x)
    Mxs.append( Mx )
print (Mxs)
plt.figure()
plt.hist(Mxs,bins=40,range=[30,70])
plt.show()