# code
# importing modules
import pandas as pd
import numpy as np

#creating dictionary of data
dic_data = {'employee_id':np.arange(1,21),
				'value':np.random.randn(20)}

# creating DataFrame from dictonary
df = pd.DataFrame(dic_data)
print(df)
