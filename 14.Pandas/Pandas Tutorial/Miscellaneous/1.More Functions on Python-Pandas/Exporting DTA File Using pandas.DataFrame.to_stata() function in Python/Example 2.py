# importing package
import pandas as pd

# create and view data
df = pd.DataFrame({
	'mobiles': ["Apple", "MI", "Karban", "JIO"],
	'prizes': [75000, 9999, 6999, 5999]
})
display(df)

# use pandas.DataFrame.to_stata method
# to extract .dta file
df.to_stata('mobiles.dta')
