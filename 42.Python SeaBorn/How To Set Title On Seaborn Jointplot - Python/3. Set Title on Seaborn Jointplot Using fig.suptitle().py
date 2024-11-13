import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('tips')
joint = sns.jointplot(data=df, x='tip', y='total_bill', palette='Set2', hue='sex')
# Set axis labels
joint.set_axis_labels('Tip Amount', 'Total Bill')
# Set title
joint.fig.suptitle('Sample Joint Plot in Seaborn', weight='bold', size=18)
joint.fig.tight_layout()

# Move the title slightly higher to avoid overlap
joint.fig.subplots_adjust(top=0.95)
plt.show()
