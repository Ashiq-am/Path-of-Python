# Take a subset of the King County, Washington
# Tax data, for Assessed Value for Tax purposes
# < $600, 000 and Total Living Sq. Feet > 100 &
# < 2000

data = data.loc[(data['TaxAssessedValue'] < 600000) &
				(data['SqFtTotLiving'] > 100) &
				(data['SqFtTotLiving'] < 2000)]
