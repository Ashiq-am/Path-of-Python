import pandas as pd

# initialize country
Course = ["DSA", "OOPS", "DBMS", "Computer Network",
		"System design", ]

# perform period_range() function
webinar_month = pd.period_range('8/1/2020', '12/1/2020', freq='M')

# genrates dataframes
df = pd.DataFrame(Course, index=webinar_month, columns=['Course'])

df
