data = {
    'Year': [2018, 2019, 2020, 2021, 2022],
    'Sales': [200, 220, 250, 275, 300]
}
df = pd.DataFrame(data)
#df.plot(x='Year', y='Sales', legend=True, label='Sales Data')

# Positioning the legend using the 'loc' parameter
df.plot(x='Year', y='Sales', legend=True, label='Sales Data', figsize=(8,6)).legend(loc='upper left')
plt.show()
