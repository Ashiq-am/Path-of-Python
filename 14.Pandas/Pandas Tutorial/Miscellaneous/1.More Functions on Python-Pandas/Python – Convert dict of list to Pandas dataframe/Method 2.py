# import pandas module
import pandas as pd

# create a dictionary for three subjects with list
# of three subjects for each student
data = {
	'manoj': ["java", "php", "python"],
	'tripura': ["bigdata", "c/cpp", "R"],
	'uma': ["js/css/html", "ruby", "IOT"]
}

# convert to dataframe using series with items() method
pd.DataFrame({key: pd.Series(val) for key, val in data.items()})
