# importing the module
import pandas as pd

# creating the series
s = pd.Series(np.take(list('0123456789'), np.random.randint(10, size = 40)))

# displaying the series
print(s)

# finding the unique count
s.value_counts()
