# import numpy as np
import matplotlib.pyplot as plt

labels = ('Busia', 'Kisumu', 'Kakamega', 'Nairobi', 'Migori')
values = (5000, 14000, 9000, 50000, 14905)

plt.pie(values, labels = labels, autopct = "%.2f%%", shadow = True)#autopct for percentage
plt.title("Number of voters in each county")
plt.savefig("Pie Chart.png")
plt.show()