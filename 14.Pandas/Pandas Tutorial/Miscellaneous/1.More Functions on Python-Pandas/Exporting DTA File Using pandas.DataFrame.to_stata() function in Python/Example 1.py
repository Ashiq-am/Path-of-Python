# importing package
import numpy
import pandas as pd

# create and view data
df = pd.DataFrame({
	'person': ["Rakesh", "Kishan", "Adesh", "Nitish"],
	'weight': [50, 60, 70, 80]
})
display(df)

# use pandas.DataFrame.to_stata method
# to extract .dta file
df.to_stata('person.dta')
