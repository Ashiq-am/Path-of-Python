import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')

# Create figure and axes
fig, ax = plt.subplots()

# Plot data
sns.scatterplot(data=tips, x='total_bill', y='tip', ax=ax)

# Load and display background image using figimage
bg_image = plt.imread('/content/gfglogo.png')
fig.figimage(bg_image, resize=True, alpha=0.5)

plt.show()
