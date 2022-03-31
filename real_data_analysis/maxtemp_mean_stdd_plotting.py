import numpy as np
import matplotlib.pyplot as plt

mean_max = np.mean(temp_max)
sigma_max = np.std(temp_max)
simulation_max = np.random.normal(mean_max, sigma_max, N)

plt.figure()
def gauss_exp(x, mean_max, sigma_max):
    return np.exp(-((x-mean_max)/sigma_max)**2/2)/(sigma_max*np.sqrt(2*np.pi))

x = np.arange(0, 40.1, 0.1)
y = gauss_exp(x, mean_max, sigma_max)
plt.plot(x, y, label='Experimental Gauss', c="red")

plt.hist(temp_max, bins=20,range=[0,40],density=True, label='real data', histtype='bar', color='pink')
plt.hist(simulation_max, bins=20,range=[0,40],density=True, label='random selection', histtype='step', linewidth=3, color='green')
plt.legend()
plt.show()