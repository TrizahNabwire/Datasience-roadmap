# Mean value(mu)
#Standard deviation (sigma)
import numpy as np
import matplotlib.pyplot as plt
from random import *

mu, sigma = 172, 4
x = mu, sigma * np.random.randn(10000)#randn generates values for a standard normal distribution
#randn supposed to get a bell curve of values
plt.hist(x, 10, density = True, facecolor = "blue")#density to True means y values will sum up to one and viewed as percentages

plt.xlabel("Students")
plt.ylabel("Scores")
plt.title("Students Scores")
plt.text(160, 0.125, "a = 172, b = 2")
plt.axis([100,190,0,0.15])#x values range from 100 to 190 and y value from 0 to 0.15
plt.grid(True)
plt.show()