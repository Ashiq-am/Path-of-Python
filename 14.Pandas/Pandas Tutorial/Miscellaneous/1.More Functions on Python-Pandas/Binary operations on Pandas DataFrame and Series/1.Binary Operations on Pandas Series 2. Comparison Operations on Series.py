import pandas as pd
s1 = pd.Series([10, 20, 30])
s2 = pd.Series([10, 25, 30])

# Comparing the two Series
result = s1 == s2
print(result)