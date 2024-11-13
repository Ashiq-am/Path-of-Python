import matplotlib.pyplot as plt

# data to display on plots

x = [3, 1, 3]
y = [3, 2, 1]
z = [1, 3, 1]

# adding the subplots
axes1 = plt.subplot2grid(
    (7, 1), (0, 0), rowspan=2, colspan=1)

axes2 = plt.subplot2grid(
    (7, 1), (2, 0), rowspan=2, colspan=1)

axes3 = plt.subplot2grid(
    (7, 1), (4, 0), rowspan=2, colspan=1)

# plotting the data
axes1.plot(x, y)
axes2.plot(x, z)
axes3.plot(z, y)
