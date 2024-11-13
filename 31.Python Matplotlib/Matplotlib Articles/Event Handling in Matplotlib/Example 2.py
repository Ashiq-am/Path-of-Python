def draw_click(self, event):
    # you can specified your own color list
    col = ['magneta', 'lavender', 'salmon', 'yellow', 'orange']
    cn = random.randint(0, 5)

    # size = square (4 * duration of the time button
    # is keep pressed )
    size = 4 * (self.end_time - self.start_time) ** 2

    # create a point of size=0.002 where mouse button
    # clicked on the plot
    c1 = plt.Circle([event.xdata, event.ydata], 0.002, )

    # create a circle of radius 0.02*size
    c2 = plt.Circle([event.xdata, event.ydata], 0.02 *
                    size, alpha=0.2, color=col[cn])
    event.canvas.figure.gca().add_artist(c1)
    event.canvas.figure.gca().add_artist(c2)
    event.canvas.figure.show()
