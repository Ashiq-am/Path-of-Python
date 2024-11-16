import pandas as pd

con = pd.Series(list('abcba'))
print(pd.get_dummies(con))
