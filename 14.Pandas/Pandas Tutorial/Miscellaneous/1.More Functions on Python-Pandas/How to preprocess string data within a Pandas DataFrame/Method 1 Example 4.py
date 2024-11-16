dataset['State'] = dataset['CovidData'].str.extract('([A-Za-z]+)', expand=True)
dataset['State']
