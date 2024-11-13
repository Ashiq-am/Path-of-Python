import numpy as np
import pandas as pd

data = pd.DataFrame({'approval': [10, 20, 30, 40, 50],
					'temperature': [(18.18, 2.27, 3.23),
									(36.43, 34.24, 6.6),
									(5.25, 6.16, 7.7),
									(7.37, 28.8, 8.9),
									(12, 23, 3)]})

res = data['temperature'].apply(lambda x: x[2]).values

print(data)
print(res)
