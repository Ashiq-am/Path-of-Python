# Series from dictionary
import pandas as pd
import numpy as np


marks = {'Maths' : 100., 'Physics' : 90.,
		'Chemistry' : 85.}
series = pd.Series(marks)

print(series)
print(type(series))

print("\nConvert Pandas Series to Python list")
print(series.tolist())
print(type(series.tolist()))
