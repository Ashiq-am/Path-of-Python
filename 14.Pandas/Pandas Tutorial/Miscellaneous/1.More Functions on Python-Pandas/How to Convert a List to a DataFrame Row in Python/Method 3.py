# import pandas module
import pandas as pd

# conside a list
list1 = [["durga", "java", 90], ["gopi", "python", 80],
		["pavani", "c/cpp", 94], ["sravya", "html", 90]]

# convert the list into dataframe row by adding columns
data = pd.DataFrame(list1, columns=['student1',
									'subject',
									'marks'])


# display
data
