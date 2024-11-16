# import pandas module
import pandas as pd

# conside a list
list1 = ["durga", "ramya", "sravya"]

list2 = ["java", "php", "mysql"]

list3 = [67, 89, 65]

# convert the list into dataframe row by
# using dictionary
dictionary = {'name': list1, 'subject': list2,
			'marks': list3}

data = pd.DataFrame(dictionary)

# display
data
