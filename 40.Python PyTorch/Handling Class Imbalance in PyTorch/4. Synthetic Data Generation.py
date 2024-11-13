from imblearn.over_sampling import SMOTE
import numpy as np
import torch

X = np.random.randn(1000, 10)
y = np.array([0]*900 + [1]*100)

smote = SMOTE()
X_res, y_res = smote.fit_resample(X, y)

# Convert back to PyTorch tensors
X_res = torch.tensor(X_res, dtype=torch.float32)
y_res = torch.tensor(y_res, dtype=torch.long)

print(X_res, y_res)
