# Customizing boxplots with color and layout
plt.boxplot(data_dict.values(), labels=data_dict.keys(), patch_artist=True,
            boxprops=dict(facecolor='lightblue', color='darkblue'),
            medianprops=dict(color='red'),
            whiskerprops=dict(color='green'))

plt.title("Customized Boxplots")
plt.xlabel("Groups")
plt.ylabel("Values")
plt.show()
