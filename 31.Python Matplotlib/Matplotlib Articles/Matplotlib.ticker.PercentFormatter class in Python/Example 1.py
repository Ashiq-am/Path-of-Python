import pandas as pd
import numpy as np
import matplotlib.ticker as mtick
from matplotlib.ticker import PercentFormatter

df = pd.DataFrame(np.random.randn(100, 5))

ax = df.plot()
ax.yaxis.set_major_formatter(mtick.PercentFormatter(5.0))
