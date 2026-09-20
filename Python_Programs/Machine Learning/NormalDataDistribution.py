import numpy as np
import matplotlib.pyplot as plt

mean = float(input("Enter mean: "))
std = float(input("Enter standard deviation: "))
values = np.random.normal(mean, std, 1000)
plt.hist(values, bins=30)
plt.show()
