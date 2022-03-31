# 

import numpy as np
import matplotlib.pyplot as plt

N = 50
t = np.random.standard_normal(N)
Mt = np.mean(t)
Sigma_t = np.std(t)
Interval_t = [Mt-(1.96*(Sigma_t)/np.sqrt(N)),Mt+(1.96*(Sigma_t)/np.sqrt(N))]

print('1) experimental mean:', Mt)
print('2) experimental standard deviation:',Sigma_t)
print('3) confidence interval:',Interval_t)
print('4) histogram with 20 bands on [-4,4]:')

def gauss(x1):
    return np.exp(-x1**2/2)/np.sqrt(2*np.pi)

def gauss_exp(x2, Mt, Sigma_t):
    return np.exp(-((x2-Mt)/Sigma_t)**2/2)/(Sigma_t*np.sqrt(2*np.pi))

x1 = np.arange(-4, 4.1, 0.1)
y1 = gauss(x1)

x2 = np.arange(-4, 4.1, 0.1)
y2 = gauss_exp(x2, Mt, Sigma_t)

plt.figure()
plt.hist(t, bins=20, range=[-4,4], density=1)
plt.plot(x1, y1, label='Theoretical Gauss', c="pink")
plt.plot(x2, y2, label='Experimental Gauss', c="red")
plt.legend()
plt.show()