dataset['confirmed_cases'] = dataset['CovidData'].str.extract(
	'(\d+.\d)', expand=True)
dataset['confirmed_cases']
