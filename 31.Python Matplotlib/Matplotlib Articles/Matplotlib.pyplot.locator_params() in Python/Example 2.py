# importing libraries
import matplotlib.pyplot as plt


# defining the function
def for_lines(xlab, ylab, plot_title,size_x, size_y, content=[]):


    width = len(content[0][1:])
    s = [x for x in range(1, width + 1)]

    # specifying the size of figure
    plt.figure(figsize=(size_x, size_y))



    for line in content:
        plt.plot(s, line[1:], 'ro--',color='green',label=line[0])

    # to add title to the plot
    plt.title(plot_title)

    # for adding labels to the plot


    plt.xlabel(xlab)
    plt.ylabel(ylab)


    t = len(s)
    plt.locator_params(nbins=t)

for_lines("x-axis", "y-axis","GeeksForGeeks", 7, 7,[[1, 2, 4, 3, 5]])
