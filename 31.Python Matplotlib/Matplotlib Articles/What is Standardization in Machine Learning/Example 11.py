import matplotlib
import matplotlib.pyplot as plt

plt.scatter(dataset_0, final_z_score, label="stars",
            color="blue", marker="*", s=30)

plt.xlabel('x - axis')
plt.ylabel('y - axis')

plt.title('Original Values')
plt.legend()

plt.show()
