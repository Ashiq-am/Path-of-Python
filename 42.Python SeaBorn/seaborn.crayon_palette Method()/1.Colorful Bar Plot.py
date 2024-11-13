import seaborn as sns
import matplotlib.pyplot as plt

colors = ['Red', 'Blue', 'Green', 'Yellow', 'Orange']
frequency = [20, 15, 25, 18, 12]

palette = sns.crayon_palette(colors)

sns.barplot(x=colors, y=frequency, palette=palette)
plt.show()
