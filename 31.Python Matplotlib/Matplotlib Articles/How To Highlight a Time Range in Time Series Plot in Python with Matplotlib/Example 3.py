# import required modules
import random
import matplotlib.pyplot as plt

# create dataset
x = [int(i) for i in range(2000,2020)]
y = [i for i in range(20)]

# depict illustration
fig, ax = plt.subplots(figsize=(10, 10))
ymin, ymax = plt. ylim()
ax.plot(x, y)

# highlight a time range
ax.axvspan(2005, 2010, color="green", alpha=0.6)
plt.show()
