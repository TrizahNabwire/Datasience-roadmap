import numpy as np
import matplotlib.pyplot as plt
Trizah = (90, 38, 69, 78, 32)
Ian = (54, 79, 69, 84, 58)
Blandyn = (44, 98, 32, 78, 64)
Daisy = (78, 74, 78, 62, 22)

skills = ("C", "C++", "Java", "Python", "Networking")

width = 0.2 # bar width
index = np.arange(5) #Array with indices one to five
#bar function used to plot bar chart
plt.bar(index, Trizah, width= width, label= "Trizah")
plt.bar(index+width, Ian, width = width, label = "Ian")
plt.bar(index + width * 2, Blandyn, width = width, label = "Blandyn")
plt.bar(index + width * 3, Daisy, width = width , label = "Daisy")

plt.xticks(index + width*2, skills)# xticks labels the xticks
plt.ylim(0, 120)#limit of the y-axis to 120 to free up some space for legend
plt.title("IT Skill Levels")
plt.ylabel("Skill Level")
plt.xlabel("IT Skill")
plt.legend()
plt.show()