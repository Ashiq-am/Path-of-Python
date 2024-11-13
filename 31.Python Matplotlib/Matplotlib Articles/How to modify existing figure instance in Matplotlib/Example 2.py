import matplotlib.pyplot as plt

# plotting a yellow background
# graph with dpi => 50
plt.figure(num='label',
		facecolor='yellow',
		figsize=[10, 7],
		dpi=50)

plt.plot([2.5, 1, 2.5, 4, 2.5],
		[1, 2.5, 4, 2.5, 1])
