import matplotlib.pyplot as plot

x = [1, 2, 3, 4, 5, 6]
y = [0, 2, 4, 6, 8, 10]

# plotting a plot
plot.plot(x, y)


# Change the x, y axis label to 'Gabriola' style.
plot.xlabel("Years", fontname="Gabriola", fontsize=18)
plot.ylabel("Population (million)", fontname="Gabriola", fontsize=18)

# Set the title to 'Franklin Gothic Medium' style.
plot.title("Line Graph - Geeksforgeeks",
		fontname='Franklin Gothic Medium', fontsize=18)

plot.show()
