# Plot the median values as red dots
medians = df.groupby('Category')['Values'].median()
for i in range(len(medians)):
    plt.plot(i, medians[i], 'ro')  # 'ro' is red color with circle marker

plt.title('Boxplot with Highlighted Median Values')
plt.show()
