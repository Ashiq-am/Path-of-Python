def change_bar_width(ax, new_width):
    for patch in ax.patches:
        current_width = patch.get_width()
        diff = current_width - new_width
        patch.set_width(new_width)
        patch.set_x(patch.get_x() + diff * .5)

# Create a barplot
ax = sns.barplot(x='Category', y='Values', data=df, palette=colors)
change_bar_width(ax, 0.5)
plt.show()
