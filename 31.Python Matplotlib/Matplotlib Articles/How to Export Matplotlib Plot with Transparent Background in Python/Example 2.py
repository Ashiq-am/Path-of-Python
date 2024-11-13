#import matplotlib
import matplotlib.pyplot as plt

#import pandas
import pandas as pd

# create a dataframe with 2 columns
data = pd.DataFrame({'data1': [1, 2, 3, 4, 21],
					'data2': [6, 7, 8, 9, 10],
					'data3': [56, 7, 8, 41, 10]})

# plot one by one
plt.plot(data['data1'])
plt.plot(data['data2'])
plt.plot(data['data3'])

# set y label
plt.ylabel('Distance')

# set x label
plt.xlabel('Time')

# set title
plt.title('Travelling')

# display plot
plt.show()

# export it
plt.savefig('image.png', transparent=True)
