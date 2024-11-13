# Generate another set of random bivariate data
data2 = np.random.multivariate_normal([1, 1], [[1, 0.5], [0.5, 1]], size=300)

# Create KDE plots for both datasets with the same contour levels
sns.kdeplot(x=data[:, 0], y=data[:, 1], levels=[0.1, 0.5, 0.9], cmap="Blues", label="Dataset 1")
sns.kdeplot(x=data2[:, 0], y=data2[:, 1], levels=[0.1, 0.5, 0.9], cmap="Reds", label="Dataset 2")
plt.legend()
plt.show()
