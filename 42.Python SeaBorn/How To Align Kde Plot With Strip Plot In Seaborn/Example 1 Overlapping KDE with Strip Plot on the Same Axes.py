import seaborn as sns
import matplotlib.pyplot as plt
data = sns.load_dataset("iris")

fig, ax = plt.subplots(figsize=(8, 6))
# Plot a strip plot
sns.stripplot(x="species", y="sepal_length", data=data, ax=ax, jitter=True, color="blue", alpha=0.6)
# Plot a KDE plot for each species
species = data['species'].unique()
for sp in species:
    subset = data[data['species'] == sp]
    sns.kdeplot(subset['sepal_length'], ax=ax, label=sp, fill=True, alpha=0.4)
plt.show()
