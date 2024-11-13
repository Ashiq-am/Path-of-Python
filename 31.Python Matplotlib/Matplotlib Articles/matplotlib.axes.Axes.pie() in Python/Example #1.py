# Implementation of matplotlib function
import matplotlib.pyplot as plt

labels = 'Geek1', 'Geek2', 'Geek3', 'Geek4'
sizes = [10, 20, 30, 40]
explode = (0.1, 0, 0, 0)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode = explode,
		labels = labels, autopct ='% 1.1f %%',
		shadow = True, startangle = 90)
ax1.axis('equal')

ax1.set_title('matplotlib.axes.Axes.pie Example')
plt.show()
