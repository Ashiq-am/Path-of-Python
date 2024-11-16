data = {
    'Year': [2018, 2019, 2020, 2021, 2022],
    'Sales': [200, 220, 250, 275, 300],
    'Profit': [50, 55, 65, 70, 80]
}
df = pd.DataFrame(data)

# Customizing Subplots
df.plot(x='Year', y=['Sales', 'Profit'], subplots=True, layout=(2, 1), sharex=True)

plt.suptitle('Sales and Profit Data Analysis')
plt.xlabel('Year')  # This won't apply directly in the subplot; you would set labels for each plot individually
plt.show()
