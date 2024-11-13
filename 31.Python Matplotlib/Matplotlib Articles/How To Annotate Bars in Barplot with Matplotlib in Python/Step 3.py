# Defining the plot size
plt.figure(figsize=(8, 8))

# Defining the values for x-axis, y-axis
# and from which datafarme the values are to be picked
plots = sns.barplot(x="Name", y="Marks", data=df)

# Iterrating over the bars one-by-one
for bar in plots.patches:
    # Using Matplotlib's annotate function and
    # passing the coordinates where the annotation shall be done
    # x-coordinate: bar.get_x() + bar.get_width() / 2
    # y-coordinate: bar.get_height()
    # free space to be left to make graph pleasing: (0, 8)
    # ha and va stand for the horizontal and vertical alignment
    plots.annotate(format(bar.get_height(), '.2f'),
                   (bar.get_x() + bar.get_width() / 2,
                    bar.get_height()), ha='center', va='center',
                   size=15, xytext=(0, 8),
                   textcoords='offset points')

# Setting the label for x-axis
plt.xlabel("Students", size=14)

# Setting the label for y-axis
plt.ylabel("Marks Secured", size=14)

# Setting the title for the graph
plt.title("This is an annotated barplot")

# Fianlly showing the plot
plt.show()
