# importing module
import matplotlib.pyplot as plt

# assigning x and y coordinates
z = [i for i in range(0, 6)]

for i in range(0, 11, 2):
    # depicting the visualization
    plt.plot(z, z, color='green', alpha=i / 10)
    plt.xlabel('x')
    plt.ylabel('y')

    # displaying the title
    print('\nIllustration with alpha =', i / 10)

    plt.show()
