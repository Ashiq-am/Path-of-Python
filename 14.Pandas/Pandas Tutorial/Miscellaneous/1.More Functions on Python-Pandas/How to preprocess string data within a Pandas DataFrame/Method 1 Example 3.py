dataset['LastUpdated'] = dataset['CovidData'].str.extract(
	'(....-..-.. ..:..:..)', expand=True)
dataset['LastUpdated']
