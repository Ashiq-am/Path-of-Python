ax2 = ax1.twinx()

# Create a lineplot for new subscribers
sns.lineplot(x='Month', y='New Subscribers', data=df, ax=ax2, color='coral', marker='o')
ax2.set_ylabel('New Subscribers')
