import matplotlib.transforms as transforms

# Create a swarmplot
ax = sns.swarmplot(data=df, x='day', y='total_bill')

# Apply a transform to shift one group
trans = transforms.Affine2D().translate(0.3, 0)  # Shifts by 0.3 on the x-axis
ax.collections[3].set_transform(trans + ax.transData)

plt.show()
