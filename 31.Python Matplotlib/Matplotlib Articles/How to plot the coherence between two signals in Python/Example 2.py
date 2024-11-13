import numpy as np
import matplotlib.pyplot as plt


# signal 1
time1 = np.arange(0, 100, 0.1)
sinsignal1 = np.sin(time1)

plt.plot(sinsignal1)
plt.title("Sine Signal")
plt.show()

# signal 2
time2 = np.arange(0, 100, 0.1)
cossignal2 = np.cos(time2)

plt.plot(cossignal2)
plt.title("Cose Signal")
plt.show()

# Store the value of correlation in
# a variable say 'cor' using the
# following code
cor = plt.cohere(sinsignal1, cossignal2)

# Plot the coherence graph
plt.show()
