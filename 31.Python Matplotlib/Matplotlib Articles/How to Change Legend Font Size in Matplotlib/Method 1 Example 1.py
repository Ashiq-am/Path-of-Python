import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize = (8, 4))

x = ['Arjun', 'Bharath', 'Raju', 'Seeta', 'Ram']
y = [5, 7, 8, 4, 6]

plt.bar(x, y, color = 'g')

plt.xlabel('Students', fontsize = 18)
plt.ylabel('Marks', fontsize = 18)

#Default fontsize of text using legend
plt.legend(['Marks scored'])

plt.show()
