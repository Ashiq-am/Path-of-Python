# importing matplotlib library
import matplotlib.pyplot as plt

# making points to be plotted on x-axis and y-axis
X_axis = [i for i in range (10, 110, 10)]
Y_axis = [2*j+5 for j in range (10, 110, 10)]

# printing points to be plotted on the x and y-axis
print("Points on x-axis are: ", X_axis)
print("Points on y-axis are: ", Y_axis)

plt.figure(figsize = ( 8, 6))
plt.tick_params(left = False)
plt.plot(X_axis, Y_axis)
plt.scatter(X_axis, Y_axis)
plt.show()
