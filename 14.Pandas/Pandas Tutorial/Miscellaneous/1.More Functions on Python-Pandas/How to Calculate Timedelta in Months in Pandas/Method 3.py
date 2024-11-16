# import packages and libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# creating a dataframe
data = pd.DataFrame({'startdate': [pd.Timestamp('20181211'),
								pd.Timestamp('20180701')],
					'enddate': [pd.Timestamp('20190612'),
								pd.Timestamp('20190712')]})

def time_delta_month(end, start):
	return 12 * (end.dt.year - start.dt.year) \
		+ (end.dt.month - start.dt.month)

print(time_delta_month(data['enddate'], data['startdate']))
