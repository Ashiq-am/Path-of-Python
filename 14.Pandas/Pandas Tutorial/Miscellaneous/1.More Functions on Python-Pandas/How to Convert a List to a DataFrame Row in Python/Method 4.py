# import pandas module
import pandas as pd

# conside a list
list1 = ["durga", "ramya", "sravya"]
list2 = ["java", "php", "mysql"]
list3 = [67, 89, 65]

# convert the list into dataframe row by
# using zip()
data = pd.DataFrame(list(zip(list1, list2, list3)),
					columns=['student', 'subject', 'marks'])


# display
data
