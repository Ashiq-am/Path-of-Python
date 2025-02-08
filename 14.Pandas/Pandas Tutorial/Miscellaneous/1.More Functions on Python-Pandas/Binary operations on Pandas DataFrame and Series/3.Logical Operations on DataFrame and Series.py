import pandas as pd
s1 = pd.Series([True, False, True])
s2 = pd.Series([False, False, True])

# Applying logical AND
result = s1 & s2
print(result)