# Example with a wider range of values
data = {'Category': ['A', 'B', 'C', 'D'],
        'Values': [10, 200, 1500, 25000]}

df = pd.DataFrame(data)

sns.barplot(x='Category', y='Values', data=df)
plt.yscale('log')  # Set the y-axis to a logarithmic scale
plt.show()
