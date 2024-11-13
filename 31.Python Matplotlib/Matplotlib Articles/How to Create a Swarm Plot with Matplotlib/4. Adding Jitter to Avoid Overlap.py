def add_jitter(x, scale=0.05):
    return x + np.random.uniform(-scale, scale, size=len(x))

df['Jittered_Category'] = df['Category'].apply(lambda x: categories.index(x))
df['Jittered_Category'] = add_jitter(df['Jittered_Category'])

# Create a scatter plot with jittered points
plt.scatter(df['Jittered_Category'], df['Value'], alpha=0.7)
plt.xticks(ticks=range(len(categories)), labels=categories)
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Swarm Plot with Jittered Points')
plt.show()
