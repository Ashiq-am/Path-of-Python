#import matplotlib
import matplotlib.pyplot as plt

# import pandas module
import pandas as pd

# create a dataframe with two columns
data = pd.DataFrame({'data1': [1, 2, 3, 4, 21],
					'data2': [6, 7, 8, 9, 10]})

# plot one by one
plt.plot(data['data1'])
plt.plot(data['data2'])

# set y label
plt.ylabel('Distance')

# set x label
plt.xlabel('Time')

# set title
plt.title('Travelling')

# display plot
plt.show()
