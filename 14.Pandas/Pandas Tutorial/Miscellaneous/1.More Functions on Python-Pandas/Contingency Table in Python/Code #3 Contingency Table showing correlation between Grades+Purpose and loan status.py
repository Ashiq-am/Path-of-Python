data_crosstab = pd.crosstab([data.grade, data.purpose],
							data.loan_status, margins = False)
print(data_crosstab)
