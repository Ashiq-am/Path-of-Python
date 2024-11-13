# importing the modules
import matplotlib.pyplot as plt


# creating data and plotting a histogram
x =[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
plt.hist(x)

# saving the figure.
plt.savefig("squares1.png",
			bbox_inches ="tight",
			pad_inches = 1,
			transparent = True,
			facecolor ="g",
			edgecolor ='w',
			orientation ='landscape')

plt.show()
