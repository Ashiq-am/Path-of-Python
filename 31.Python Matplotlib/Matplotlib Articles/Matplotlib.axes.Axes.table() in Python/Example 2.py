# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

data = [[66, 174, 71, 58],
        [58, 139, 45, 164],
        [89, 52, 18, 81],
        [78, 58, 123, 68],
        [13, 159, 164, 80]]

val1 = ('Geek1', 'Geek2', 'Geek3', 'Geek4')
val2 = ['Month % d' % x for x in (5, 4, 3, 2, 1)]
val3 = np.arange(0, 2500, 500)
val4 = 1000
val5 = plt.cm.plasma(np.linspace(0, 0.5, len(val2)))
val6 = len(data)
val7 = np.arange(len(val1)) + 0.3
val8 = 0.4
val9 = np.zeros(len(val1))

lista = []

fig, ax = plt.subplots()

for row in range(val6):
    ax.bar(val7, data[row], val8, bottom=val9,
           color=val5[row])
    val9 = val9 + data[row]

    lista.append([(x // 50) for x in val9])

the_table = ax.table(cellText=lista,
                     rowLabels=val2,
                     rowColours=val5,
                     colLabels=val1,
                     loc='bottom')

plt.subplots_adjust(left=0.2, bottom=0.2)

ax.set_xticks([])

ax.set_title('matplotlib.axes.Axes.table() function Example',
             fontweight="bold")

plt.grid()
plt.show()
