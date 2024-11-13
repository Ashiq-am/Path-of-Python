import matplotlib.pyplot as plt

data1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
data2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
data3 = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

datasets = [data1, data2, data3]
labels = ['Dataset 1', 'Dataset 2', 'Dataset 3']
colors = ['blue', 'orange', 'green']

fig, ax = plt.subplots()

for data, label, color in zip(datasets, labels, colors):
    bp = ax.boxplot(data, patch_artist=True)
    for patch in bp['boxes']:
        patch.set_facecolor(color)
        patch.set_label(label)

ax.legend()
plt.title("Multiple Boxplots with Legend")
plt.show()
