# Here We are checking the Graph
# of the Original Values
plt.scatter(dataset_0, dataset_1, label="stars",
            color="blue", marker="*", s=40)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.legend()
plt.show()

# Here we are checking the Graph of
# the Standardized Values
plt.scatter(dataset_0, final_z_score, label="stars",
            color="blue", marker="*", s=30)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.legend()
plt.show()
