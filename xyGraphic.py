import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')#grid

xValues = np.linspace(0, 10, 100)
yValues = np.sin(xValues)
yyValues = np.cos(xValues)
#labeling
plt.title("A graph showing number of registered voters in each county")
plt.suptitle("Right to vote your leaders")
plt.grid(True)
plt.xlabel("County")
plt.ylabel("Registered voters")


plt.plot(xValues, yValues, 'b', label = "Registered voters")
plt.plot(xValues, yyValues, 'v', label = "Unregistered voters")
plt.legend(loc = 'upper right')#legend used for labeling elements for readability

plt.savefig("Voters.png")#savefig saves your diagram
plt.show()

