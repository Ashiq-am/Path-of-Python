# importing matplot library along
# with necessary modules
import matplotlib.pyplot as plt


# providing values to x and y
x = [8, 5, 11, 13, 16, 23]
y = [14, 8, 21, 7, 12, 15]

# to plot x and y
#plt.plot(x, y)
# to generate window of custom
# dimensions [left, bottom, width,
# height] along with the facecolor
plt.axes([0, 2.0, 2.0, 2.0], facecolor = 'black')
