import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.mosaicplot import mosaic

data = {
    'gender': ['male', 'male', 'male', 'female', 'female', 'female'],
    'pet': ['cat', 'dog', 'dog', 'cat', 'dog', 'cat']
}
df = pd.DataFrame(data)

# Create mosaic plot from DataFrame
mosaic(df, ['pet', 'gender'])
plt.show()
