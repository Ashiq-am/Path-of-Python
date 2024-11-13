import matplotlib.pyplot as plt

plt.ion()
plt.plot([1.4, 2.5])
plt.title(" Sampple interactive plot")

axes = plt.gca()
axes.plot([3.1, 2.2])
