import matplotlib.pyplot as plt


fig = plt.figure()

axes1 = plt.subplot2grid((4, 4), (0, 0),
						colspan = 4)

axes2 = plt.subplot2grid((4, 4), (1, 0),
						colspan = 3)

axes3 = plt.subplot2grid((4, 4), (1, 2),
						rowspan = 3)

axes4 = plt.subplot2grid((4, 4), (2, 0))
axes5 = plt.subplot2grid((4, 4), (2, 1))

fig.tight_layout()
