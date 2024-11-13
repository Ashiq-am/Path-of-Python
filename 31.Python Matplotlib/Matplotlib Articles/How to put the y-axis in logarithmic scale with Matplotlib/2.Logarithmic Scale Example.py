import matplotlib.pyplot as plt

data = [10**i for i in range(4)]

# convert y-axis to Logarithmic scale
plt.yscale("log")
plt.plot(data)
