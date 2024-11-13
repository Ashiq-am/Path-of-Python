ax = sns.boxplot(x='day', y='total_bill', data=tips)
# Set the title with custom appearance
ax.set_title('Customized Boxplot Title', fontsize=16, color='blue', fontweight='bold')
plt.show()
