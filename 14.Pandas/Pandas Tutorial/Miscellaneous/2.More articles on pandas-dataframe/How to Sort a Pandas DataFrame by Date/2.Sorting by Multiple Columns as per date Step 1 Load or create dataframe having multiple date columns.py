# importing package
import pandas as pd

# Creating a DataFrame
data_1 = pd.DataFrame({'Mfg. Date': ['2021-01-25','2021-01-22','2021-01-20','2021-01-18',
					'2021-01-22','2021-01-17','2021-01-21'],
					'ProductID': [7,5,3,2,6,1,4],
					'Product Name': ['Paracetamol','Moov','Volini','Crocin',
										'Aciloc','Iodex','Combiflam'],
					'Expiry Date':['2022-01-25','2023-01-22','2021-05-20','2022-03-18',
									'2022-01-22','2021-05-17','2022-01-30']
					})

# Checking dataframe
print(data_1)
