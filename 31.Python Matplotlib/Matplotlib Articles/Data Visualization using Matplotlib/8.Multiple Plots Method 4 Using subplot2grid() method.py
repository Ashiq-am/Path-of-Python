import matplotlib.pyplot as plt

# initializing the data
x = [10, 20, 30, 40]
y = [20, 25, 35, 55]

# adding the subplots
axes1 = plt.subplot2grid (
(7, 1), (0, 0), rowspan = 2, colspan = 1)

axes2 = plt.subplot2grid (
(7, 1), (2, 0), rowspan = 2, colspan = 1)

# plotting the data
axes1.plot(x, y)
axes2.plot(y, x)
