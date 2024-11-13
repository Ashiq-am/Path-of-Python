# Implementation of matplotlib function
import matplotlib.pyplot as plt
import matplotlib.table as tbl

val1 = ["{:X}".format(i) for i in range(10)]
val2 = ["{:02X}".format(10 * i) for i in range(10)]
val3 = [["" for c in range(10)] for r in range(10)]

fig, ax = plt.subplots()
ax.set_axis_off()
table = tbl.table(
	ax,
	cellText = val3,
	rowLabels = val2,
	colLabels = val1,
	rowColours = ["palegreen"] * 10,
	colColours =["palegreen"] * 10,
	cellLoc ='center',
	loc ='upper left')

ax.add_table(table)

ax.set_title('matplotlib.axes.Axes.add_table() function Example', fontweight ="bold")

plt.show()
