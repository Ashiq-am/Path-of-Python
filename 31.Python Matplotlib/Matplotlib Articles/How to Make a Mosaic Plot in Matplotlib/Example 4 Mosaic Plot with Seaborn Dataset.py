import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.graphics.mosaicplot import mosaic

tips = sns.load_dataset('tips')

# Create mosaic plot from tips dataset
mosaic(tips, ['sex', 'smoker', 'time'])
plt.show()
