# import matplotlib.pyplot library
import matplotlib.pyplot as plt

data = [16, 25, 47, 56, 23, 45, 19, 55, 44, 27]

# separating the stem parts
stems = [1, 1, 2, 2, 2, 4, 4, 4, 5, 5]

plt.ylabel('Data') # for label at y-axis

plt.xlabel('stems') # for label at x-axis

plt.xlim(0, 10) # limit of the values at x axis

plt.stem(stems, data) # required plot
