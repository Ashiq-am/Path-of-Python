# importing pandas as pd
import pandas as pd

# Specify start and periods, the number of periods (days).
dRan1 = pd.date_range(start ='1-1-2018', periods = 13)

# Specify end and periods, the number of periods (days).
dRan2 = pd.date_range(end ='1-1-2018', periods = 13)

# Specify start, end, and periods; the frequency
# is generated automatically (linearly spaced).
dRan3 = pd.date_range(start ='01-03-2017',
			end ='1-1-2018', periods = 13)

print(dRan1, "\n\n", dRan2, '\n\n', dRan3)
