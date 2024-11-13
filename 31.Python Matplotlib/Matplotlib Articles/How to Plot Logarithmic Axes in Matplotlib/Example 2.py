import matplotlib.pyplot as plt

# exponential function y = 10^x
data = [10**i for i in range(5)]

# convert y-axis to Logarithmic scale
plt.yscale("log")

plt.plot(data)
