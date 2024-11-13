# import modules
import matplotlib.pyplot as plt
import numpy as np
from scipy.cluster.vq import whiten, kmeans, vq

# load the dataset
dataset = np.loadtxt(r"{your-path}\diabetes-train.csv",
					delimiter=",")

# excluding the outcome column
dataset = dataset[:, 0:8]

print("Data :\n", dataset, "\n")

# normalize
dataset = whiten(dataset)

# generate code book
centroids, mean_dist = kmeans(dataset, 2)
print("Code-book :\n", centroids, "\n")

clusters, dist = vq(dataset, centroids)
print("Clusters :\n", clusters, "\n")

# count non-diabetic patients
non_diab = list(clusters).count(0)

# count diabetic patients
diab = list(clusters).count(1)

# depict illustration
x_axis = []
x_axis.append(diab)
x_axis.append(non_diab)

colors = ['green', 'orange']

print("No.of.diabetic patients : " + str(x_axis[0]) +
	"\nNo.of.non-diabetic patients : " + str(x_axis[1]))

y = ['diabetic', 'non-diabetic']

plt.pie(x_axis, labels=y, colors=colors, shadow='true')
plt.show()
