import matplotlib.pyplot as plt

plt.plot([2.5, 1, 2.5, 4, 2.5],
		[1, 2.5, 4, 2.5, 1])

# This will clear the first plot
plt.figure(clear=True)

# This will make a new plot on a
# different instance
plt.plot([1, 2, 3, 4], [1, 2, 3, 4])
