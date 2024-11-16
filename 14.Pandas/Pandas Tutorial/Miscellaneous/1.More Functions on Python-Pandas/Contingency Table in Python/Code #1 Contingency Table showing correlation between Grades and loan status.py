data_crosstab = pd.crosstab(data['grade'],
							data['loan_status'],
							margins = False)
print(data_crosstab)
