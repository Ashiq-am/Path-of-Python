# import pandas
import pandas as pd
ser = pd.Series(range(1, 20, 3),
index=[x for x in 'abcdefg'])
print(ser)
