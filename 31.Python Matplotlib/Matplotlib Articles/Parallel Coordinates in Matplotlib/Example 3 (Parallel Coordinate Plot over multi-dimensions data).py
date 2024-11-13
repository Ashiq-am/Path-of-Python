# import packages
import numpy as np
import matplotlib.pyplot as plt

# create data
x = np.arange(1,6)
data = [x,x*2,x*x,np.sqrt(x),-x*x,np.sin(x),np.cos(x)]
print(data)

# make subplots
fig, (ax1,ax2,ax3,ax4) = plt.subplots(1, 4, sharey=False)
ax = (ax1,ax2,ax3,ax4)

# plot subplots and set xlimit
for i in range(4):
	for j in range(len(data)):
		ax[i].plot(data[0],data[j])
	ax[i].set_xlim([x[i],x[i+1]])

# set width space to zero
plt.subplots_adjust(wspace=0)

# show plot
plt.show()
