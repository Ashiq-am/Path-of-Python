# importing necessary libraries
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


# function to create data for plotting
def data_creation():
    # creating 3d data
    x = np.outer(np.linspace(-3, 3, 30), np.ones(30))
    y = x.copy().T  # transpose
    z = np.cos(x ** 2 + y ** 2)
    return (x, y, z)


# main function
if __name__ == '__main__':
    # creating three dimensional co-ordinate system
    ax = plt.gca(projection='3d')

    # calling data creation function and storing in
    # the variables
    data_x, data_y, data_z = data_creation()

    # changing grid lines thickness of x axis to 3
    ax.xaxis._axinfo["grid"].update({"linewidth": 3})

    # plotting surface plot
    ax.plot_surface(data_x, data_y, data_z)

    # giving label name to x,y and z axis
    ax.set_xlabel("X axis")
    ax.set_ylabel("Y axis")
    ax.set_zlabel("Z axis")

    # visualizing the plot
    plt.show()
