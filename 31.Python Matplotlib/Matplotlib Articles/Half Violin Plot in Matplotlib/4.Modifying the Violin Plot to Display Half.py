# Create a half violin plot by splitting and displaying only one side
sns.violinplot(data=data, cut=0, bw=0.2, inner=None, linewidth=1)
plt.gca().collections[0].set_clip_on(False)  # Show only one side
plt.gca().collections[0].set_alpha(0.7)      # Adjust transparency for better visibility

plt.show()
