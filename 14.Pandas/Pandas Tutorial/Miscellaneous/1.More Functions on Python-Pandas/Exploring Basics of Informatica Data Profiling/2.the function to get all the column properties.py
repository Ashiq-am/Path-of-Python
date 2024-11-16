def data_profile(i, col_name, pattern_list):

	# Total Number of Records
	Total_Records = len(data[data.columns[i]])

	# 2 Number of Null values in the column
	Number_Null = data[data.columns[i]].isnull().sum()

	# 3 Percentage Null
	Percent_Null = Number_Null / Total_Records * 100

	# 4 Number of Unique Values
	Num_Unique = data[data.columns[i]].nunique()

	# 5 Percentage Unique
	Percent_Unique = Num_Unique / Total_Records * 100

	# 6 Number of Duplicate Values
	Non_Distinct = Total_Records - Num_Unique

	# 7 Percentage of Duplicate Values
	Percent_non_distinct = Non_Distinct / Total_Records * 100

	# 8, 9, 10 - Minimum, Maximum and Average of a Integer or Float type
	if data[data.columns[i]].dtypes in ["int64", "int32", "int16", "float64", "float32", "float16"]:
		minimum = min(data[data.columns[i]])
		maximum = max(data[data.columns[i]])
		average = data[data.columns[i]].mean()
	else:
		minimum = "NA"
		maximum = "NA"
		average = "NA"

	# 11 Number of Patterns
	patterns = []
	if data[data.columns[i]].dtype == 'O':
		for value in data[data.columns[i]]:
			k = ""
			for n in range(0, len(pattern_list)):
				k = re.search(pattern_list[n], value)
				patterns.append(k)
				if k == re.Match:
					break
		patterns_1 = list(filter(lambda x: x is not None, patterns))
		Num_Pattern = len(patterns_1)
	else:
		for value in data[data.columns[i]].astype(str):
			k = ""
			for n in range(0, len(pattern_list)):
				k = re.search(pattern_list[n], value)
				patterns.append(k)
				if k == re.Match:
					break
		patterns_1 = list(filter(lambda x: x is not None, patterns))
		Num_Pattern = len(patterns_1)

	# 12 Minimum Length of the string or number
	if data[data.columns[i]].dtype == 'O':
		min_word = min(data[data.columns[i]], key=len)
		min_len = len(min_word)
	else:
		min_len = "NA"

	# 13 Maximum Length of the string or number
	if data[data.columns[i]].dtype == 'O':
		max_word = max(data[data.columns[i]], key=len)
		max_len = len(max_word)
	else:
		max_len = "NA"

	# 14 Average Length of the string
	if data[data.columns[i]].dtype == 'O':
		avg_word = data[data.columns[i]].apply(len).mean()
		avg_word = math.ceil(avg_word)
	else:
		avg_word = "NA"

	# 15 Datatype of the Column
	dtype = data[data.columns[i]].dtype
	if dtype == 'O':
		data_type = "String"
	elif dtype == 'int64':
		data_type = "int64"
	elif dtype == 'int32':
		data_type = "int32"
	elif dtype == 'int16':
		data_type = "int16"
	elif dtype == 'float64':
		data_type = "float64"
	elif dtype == 'float32':
		data_type = "float32"
	elif dtype == 'float16':
		data_type = "float16"
	elif dtype == 'bool':
		data_type = "boolean"
	else:
		data_type = dtype

	return_list = [col_name, Number_Null, Percent_Null, Num_Unique, Percent_Unique, Non_Distinct,
				Percent_non_distinct, Num_Pattern, minimum, maximum, average, min_len, max_len, avg_word, data_type]

	return return_list
