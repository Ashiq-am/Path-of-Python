data = {
    'Year': [2018, 2019, 2020, 2021, 2022],
    'Sales': [200, 220, 250, 275, 300]
}
df = pd.DataFrame(data)
# Adding Annotations
df.plot(x='Year', y='Sales')
plt.annotate('Sales Drop', xy=(2020, 250), xytext=(2019, 260),
             arrowprops=dict(facecolor='black', shrink=0.05))
plt.show()
