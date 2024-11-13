import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Create a sample dataset
np.random.seed(10)
data = pd.DataFrame({
    'Group': np.repeat(['A', 'B', 'C'], 100),
    'Values': np.concatenate([
        np.random.normal(0, 1, 100),
        np.random.normal(5, 1.5, 100),
        np.random.normal(10, 2, 100)
    ])
})
