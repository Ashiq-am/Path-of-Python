# implementation of the matplotlib function
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)

plt.rcdefaults()
fig, ax = plt.subplots()

people = ('Geek1', 'Geek2', 'Geek3', 'Geek4', 'Geek5')
y_pos = np.arange(len(people))
performance = 3 + 5 * np.random.rand(len(people))
error = np.random.rand(len(people))

ax.bar(y_pos, performance, xerr = error, align ='center')
ax.set_yticks(y_pos)
ax.set_yticklabels(people)
ax.invert_yaxis()
plt.grid(True)

plt.title('matplotlib.pyplot.rcdefaults() Example')
plt.show()
