# importing packages
import pandas.api.types as pd
import datetime
import numpy as np

date_list = np.array([datetime.datetime.today()
					+ datetime.timedelta(days=x)
					for x in range(10)],
					dtype=np.datetime64)
print(pd.is_datetime64_dtype(date_list))
