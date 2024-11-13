import matplotlib.pyplot as plt

# exponential function x = 10^y
datax = [ 10**i for i in range(5)]
datay = [ i for i in range(5)]

#convert x-axis to Logarithmic scale
plt.xscale("log")

plt.plot(datax,datay)
