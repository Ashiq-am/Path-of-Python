fig, ax1 = plt.subplots()

# Create a barplot for revenue
sns.barplot(x='Month', y='Revenue', data=df, ax=ax1, color='skyblue')
ax1.set_ylabel('Revenue')
