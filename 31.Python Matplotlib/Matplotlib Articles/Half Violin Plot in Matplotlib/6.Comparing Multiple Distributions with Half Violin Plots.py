# Generate sample data for two distributions
data1 = np.random.normal(loc=-2, scale=1, size=100)
data2 = np.random.normal(loc=2, scale=1, size=100)

fig, ax = plt.subplots()

# Plot the first half violin plot
parts1 = ax.violinplot(data1, positions=[1], showmeans=False, showmedians=True)
for pc in parts1['bodies']:
    pc.set_clip_path(plt.Rectangle((0, -np.inf), np.inf, np.inf))

# Plot the second half violin plot
parts2 = ax.violinplot(data2, positions=[2], showmeans=False, showmedians=True)
for pc in parts2['bodies']:
    pc.set_clip_path(plt.Rectangle((0, -np.inf), np.inf, np.inf))

plt.title("Comparison of Two Distributions with Half Violin Plots")
plt.show()
