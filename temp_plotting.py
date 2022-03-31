# Plotting of temperature raw data

import matplotlib.pyplot as plt

y1 = temp_min
y2 = temp_max

plt.figure()
plt.plot(x, y1, label='Minimum temperature', c="blue")
plt.plot(x, y2, label='Maximum temperature', c="red")
plt.xlabel("Years")
plt.ylabel("Temperatures")
plt.legend(fontsize='8')
plt.show()