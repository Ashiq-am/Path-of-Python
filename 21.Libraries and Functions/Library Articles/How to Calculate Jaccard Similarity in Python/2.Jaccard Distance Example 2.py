import numpy as np
from sklearn.metrics import jaccard_score

# predicted values
y_pred = np.array([1, 1, 1, 0, 1]).reshape(-1, 1)
# true values
y_true = np.array([1, 1, 0, 0, 1]).reshape(-1, 1)

# Calculate Jaccard Index
jaccard_index = jaccard_score(y_true, y_pred)

# Calculate Jaccard Distance
jaccard_distance = 1 - jaccard_index

print("Jaccard Index:", jaccard_index)
print("Jaccard Distance:", jaccard_distance)
