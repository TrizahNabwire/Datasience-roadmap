import numpy as np
import matplotlib.pyplot as plt
mu , sigma = 172, 4
values = np.random.normal(mu, sigma, 200)
plt.ylabel("Height")
plt.boxplot(values)
plt.show()