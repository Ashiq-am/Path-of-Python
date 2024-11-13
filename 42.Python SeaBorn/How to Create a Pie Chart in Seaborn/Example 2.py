# importing libraries
import matplotlib.pyplot as plt
import seaborn

# declaring data
data = [44, 45, 40, 41, 39]
keys = ['Class 1', 'Class 2', 'CLass 3', 'Class 4', 'Class 5']

# declaring exploding pie
explode = [0, 0.1, 0, 0, 0]
# define Seaborn color palette to use
palette_color = seaborn.color_palette('dark')

# plotting data on chart
plt.pie(data, labels=keys, colors=palette_color,
		explode=explode, autopct='%.0f%%')

# displaying chart
plt.show()
