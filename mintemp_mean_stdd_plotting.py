import numpy as np
import matplotlib.pyplot as plt

mean_min = np.mean(temp_min)
sigma_min = np.std(temp_min)
simulation_min = np.random.normal(mean_min, sigma_min, N)

plt.figure()
def gauss_exp(x, mean_min, sigma_min):
    return np.exp(-((x-mean_min)/sigma_min)**2/2)/(sigma_min*np.sqrt(2*np.pi))

x = np.arange(0, 40.1, 0.1)
y = gauss_exp(x, mean_min, sigma_min)
plt.plot(x, y, label='Experimental Gauss', c="blue")

plt.hist(temp_min, bins=20,range=[0,40],density=True, label='real data', histtype='bar', color='lightblue')
plt.hist(simulation_min, bins=20,range=[0,40],density=True, label='random selection', histtype='step', linewidth=3, color='orange')
plt.legend()
plt.show()