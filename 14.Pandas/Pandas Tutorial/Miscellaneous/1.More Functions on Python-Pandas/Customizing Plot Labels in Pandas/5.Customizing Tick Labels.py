data = {
    'Year': [2018, 2019, 2020, 2021, 2022],
    'Sales': [200, 220, 250, 275, 300]
}
df = pd.DataFrame(data)
# Customizing Tick Labels
df.plot(x='Year', y='Sales')
plt.xticks(fontsize=12, rotation=45)
plt.yticks(fontsize=12, color='green')
plt.show()
