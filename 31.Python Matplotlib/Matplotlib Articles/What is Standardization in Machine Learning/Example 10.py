# Now we will compare and see the graph
# of the Original Values and the
# Standardized Values
import matplotlib
import matplotlib.pyplot as plt

# Here We are checking the Graph of the
# Original Values
plt.scatter(dataset_0, dataset_1, label="stars",
			color="blue", marker="*", s=40)

plt.xlabel('x - axis')
plt.ylabel('y - axis')

plt.title('Original Values')
plt.legend()

plt.show()
