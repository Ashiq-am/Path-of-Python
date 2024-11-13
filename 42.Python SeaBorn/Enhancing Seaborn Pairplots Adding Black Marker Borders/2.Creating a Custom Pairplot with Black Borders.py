import seaborn as sns
import matplotlib.pyplot as plt
iris = sns.load_dataset("iris")

g = sns.pairplot(iris, hue="species", markers=["o", "s", "D"])
# Set black borders for specific markers
for ax in g.axes.flatten():
    for collection in ax.collections:
        if len(collection.get_offsets()) > 0 and collection.get_offsets()[0, 0] == iris[iris['species'] == 'setosa'].iloc[0, 0]:
            collection.set_edgecolor('black')

plt.show()
