import matplotlib.pyplot as plt

fig1 = plt.figure()
plt.plot([1, 2, 3], [4, 5, 6])
plt.title("Figure 1")

fig2 = plt.figure()
plt.plot([1, 2, 3], [6, 5, 4])
plt.title("Figure 2")

plt.close(fig1) # Close the first figure
plt.show() # Show remaining figures