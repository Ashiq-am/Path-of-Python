data.reset_index().plot(x='geoName', y='Cloud Computing',
						figsize=(10,5), kind="bar")
plt.style.use('fivethirtyeight')
plt.show()
