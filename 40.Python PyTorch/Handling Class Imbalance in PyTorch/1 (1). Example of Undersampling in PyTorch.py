from imblearn.under_sampling import RandomUnderSampler
import numpy as np
import torch

# Example data and targets
X = np.random.randn(1000, 10)
y = np.array([0]*900 + [1]*100)

rus = RandomUnderSampler()
X_res, y_res = rus.fit_resample(X, y)

# Convert back to PyTorch tensors
X_res = torch.tensor(X_res, dtype=torch.float32)
y_res = torch.tensor(y_res, dtype=torch.long)

print(X_res, y_res)
