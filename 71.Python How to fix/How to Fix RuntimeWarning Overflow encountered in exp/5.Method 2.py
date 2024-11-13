import numpy as np
import warnings

# suppress warnings
warnings.filterwarnings('ignore')

x = 789
x = np.float128(x)
print(np.exp(x))
