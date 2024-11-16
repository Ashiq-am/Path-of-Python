ax = df.plot(x='Year', y='Sales', color='red', legend=False)
ax2 = ax.twinx()
df['Profit'] = [50, 55, 65, 70, 80]  # Example profit data
df.plot(x='Year', y='Profit', ax=ax2, color='blue', legend=False)
ax.set_ylabel('Sales ($)')
ax2.set_ylabel('Profit ($)')
plt.show()
