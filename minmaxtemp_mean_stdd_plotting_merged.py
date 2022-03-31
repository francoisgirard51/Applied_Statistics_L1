import numpy as np
import matplotlib.pyplot as plt

mean_min = np.mean(temp_min)
sigma_min = np.std(temp_min)
mean_max = np.mean(temp_max)
sigma_max = np.std(temp_max)
simulation_min = np.random.normal(mean_min, sigma_min, N)
simulation_max = np.random.normal(mean_max, sigma_max, N)

plt.figure()
def gauss_exp_max(x_max, mean_max, sigma_max):
    return np.exp(-((x_max-mean_max)/sigma_max)**2/2)/(sigma_max*np.sqrt(2*np.pi))

x_max = np.arange(0, 40.1, 0.1)
y_max = gauss_exp_max(x_max, mean_max, sigma_max)

def gauss_exp_min(x_min, mean_min, sigma_min):
    return np.exp(-((x_min-mean_min)/sigma_min)**2/2)/(sigma_min*np.sqrt(2*np.pi))

x_min = np.arange(0, 40.1, 0.1)
y_min = gauss_exp_min(x_min, mean_min, sigma_min)

plt.plot(x_max, y_min, label='Gauss expérimentale min', c="blue")
plt.plot(x_max, y_max, label='Gauss expérimentale max', c="red")
plt.hist(temp_min, bins=20,range=[0,40],density=True, label='relevés réels', histtype='bar', color='lightblue')
plt.hist(simulation_min, bins=20,range=[0,40],density=True, label='tirage aléatoire', histtype='step', linewidth=3, color='orange')
plt.hist(temp_max, bins=20,range=[0,40],density=True, label='relevés réels', histtype='bar', color='pink')
plt.hist(simulation_max, bins=20,range=[0,40],density=True, label='tirage aléatoire', histtype='step', linewidth=3, color='green')
plt.legend(fontsize='7')
plt.show()