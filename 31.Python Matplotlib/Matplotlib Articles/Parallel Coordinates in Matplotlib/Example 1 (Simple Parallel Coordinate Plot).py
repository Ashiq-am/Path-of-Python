# import packages
import matplotlib.pyplot as plt

# create data
x=[1,2,3,4,5]
y=[2,4,1,5,3]

# make subplots
fig,(ax1,ax2) = plt.subplots(1, 2, sharey=False)

# plot the subplots
ax1.plot(x,y)
ax2.plot(x,y)

# set x limits
ax1.set_xlim([ x[0],x[2]])
ax2.set_xlim([ x[2],x[4]])

# set width space to zero
plt.subplots_adjust(wspace=0)

# show the plots
plt.show()
