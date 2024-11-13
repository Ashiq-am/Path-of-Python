import numpy as np
import matplotlib.pyplot as plt


# signal 1
time1=np.arange(0,100,0.1)
cossignal1= np.cos(time1)

plt.plot(cossignal1)
plt.title("Signal 1")
plt.show()


# signal 2
time2=np.arange(0,100,0.1)
cossignal2= np.cos(time2)

plt.plot(cossignal2)
plt.title("Signal 2")
plt.show()

# Store the value of correlation in a
# variable say 'cor' using the following code:
cor=plt.cohere(cossignal1,cossignal2)


# plot the coherence graph
plt.show()
