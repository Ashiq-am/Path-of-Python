import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn')

x = [1,2,3,4,5,6,7,8,9,10,11,12]
y = [1,2,3,4,5,6,7,8,9,10,11,12]
points_size = [100,200,300,400,500,600,700,800,900,1000,1100,1200]


plt.xticks(np.arange(13))
plt.yticks(np.arange(13))

plt.scatter(x,y,s=points_size,c='g')

plt.title("Scatter Plot with increase in size of scatter points ", fontsize=22)

plt.xlabel('x-axis',fontsize=20)
plt.ylabel('y-axis',fontsize=20)

plt.show()
