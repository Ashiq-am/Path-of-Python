import pandas as pd
import datetime
import numpy as np


dates =['14 / 05 / 2017', '2017', '07 / 09 / 2017']

frame = pd.to_datetime(dates, dayfirst = True)
frame = pd.DataFrame([frame]).transpose()
frame['date']= frame
frame['month']= frame['date'].dt.month
frame.drop(0, axis = 1, inplace = True)

frame
