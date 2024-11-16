import pandas as pd
import matplotlib.pyplot as plt

# Make example dataframe
df = pd.DataFrame([(1, 'Germany'),
				(2, 'France'),
				(3, 'Indonesia'),
				(4, 'France'),
				(5, 'France'),
				(6, 'Germany'),
				(7, 'UK'),
				(8, 'India'),
				(9, 'India'),
				(10, 'Germany')
				],
				columns=['groupid', 'country'],
				index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])


# print all unique country name in the list
su1 = df['country'].value_counts().index.tolist()
print(su1)

# print 1st unique country name present in a list
su2 = df['country'].value_counts().index.tolist()[0]
print(su2)
