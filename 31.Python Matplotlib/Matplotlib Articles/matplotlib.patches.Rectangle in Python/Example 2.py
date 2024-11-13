import matplotlib
import matplotlib.pyplot as plt


fig = plt.figure()
ax = fig.add_subplot(111)

rect1 = matplotlib.patches.Rectangle((-200, -100),
									400, 200,
									color ='green')

rect2 = matplotlib.patches.Rectangle((0, 150),
									300, 20,
									color ='pink')

rect3 = matplotlib.patches.Rectangle((-300, -50),
									40, 200,
									color ='yellow')

ax.add_patch(rect1)
ax.add_patch(rect2)
ax.add_patch(rect3)

plt.xlim([-400, 400])
plt.ylim([-400, 400])

plt.show()
