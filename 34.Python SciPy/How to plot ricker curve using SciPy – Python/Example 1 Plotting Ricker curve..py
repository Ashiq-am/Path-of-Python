from scipy import signal
import matplotlib.pyplot as plt

point = 100
hat = signal.ricker(point, 4)

fig = plt.figure(figsize = (8, 8))
ax = fig.add_subplot(1, 1, 1)

# Move left y-axis and bottim x-axis to centre,
# passing through (0,0)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

# Eliminate upper and right axes
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

plt.grid(True)
plt.plot(hat)

plt.show()
