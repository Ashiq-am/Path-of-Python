# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)
plt.rcdefaults()
fig, ax = plt.subplots()

people = ('Geek1', 'Geek2', 'Geek3',
          'Geek4', 'Geek5')

y_pos = np.arange(len(people))
performance = 3 + 4.5 * np.random.rand(len(people)) ** 2
error = np.random.rand(len(people))

ax.barh(y_pos, performance, xerr=error,
        align='center', color="green")
ax.set_yticks(y_pos)
ax.set_yticklabels(people)

ax.invert_yaxis()
ax.set_xlabel('Performance')
x = ax.yaxis_inverted()
ans = "No"
if x:
    ans = "Yes"

ax.set_title('matplotlib.axes.Axes.yaxis_inverted() \
Example\n',
             fontsize=14, fontweight='bold')
ax.text(3, -0.75, "Y-axis is inverted ? : " + ans,
        style='italic', fontsize=12)

plt.show()
