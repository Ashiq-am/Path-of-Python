ax = df.plot(x='Year', y='Sales')
plt.fill_between(df['Year'], df['Sales'], color='skyblue', alpha=0.3)
plt.show()
