# Interval confidence with test

import numpy as np
import matplotlib.pyplot as plt

# Set of draws
x1 = np.random.uniform (0, 100 , 20)
x2 = np.random.uniform (0, 100 , 100)
x3 = np.random.uniform (0, 100 , 1000)
x4 = np.random.uniform (0, 100 , 10000)

print('Mean, standard deviation and confidence interval for 20, 100, 1,000, 10,000 random draws:\n')
def caracteristic (n):
    x1 = np.random.uniform (0, 100 , n)

    # Moyenne
    Mx1 = np.mean(x1)

    # Eccart-type
    Sigma_x1 = np.std(x1)

    # Intervalle de confiance
    Interval_x1 = [Mx1-(1.96*(Sigma_x1)/np.sqrt(n)),Mx1+(1.96*(Sigma_x1)/np.sqrt(n))]

    return (Mx1,Sigma_x1,Interval_x1)
    
draws = [20, 100, 1000, 10000]

for i in draws:
    print('- ', i, caracteristic(i))
    
# TEST
# We procede to 100,000 random draws within the interval [0,100]
# We calculate the % of cases of the expected value being within the interval

frequence = 0
for i in range(100000):
    var = caracteristic(20)[2]
    if var[0] < 50 and var[1] > 50:
        frequence += 1
frequence = frequence/100000
print('\nThe expected value is in range in', frequence*100, '%\ of cases on 100,000 random draws.')
