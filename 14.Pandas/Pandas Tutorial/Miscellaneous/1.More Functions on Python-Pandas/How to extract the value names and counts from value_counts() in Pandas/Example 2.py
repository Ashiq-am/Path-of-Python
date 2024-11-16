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


# print country name and counts
su3 = df['country'].value_counts()
print(su3)

# print 1st country count in a list
su4 = df['country'].value_counts()[0]
print(su4)
