import numpy as np
import scipy.stats as st

# define sample data
gfg_data = np.random.randint(5, 10, 100)

# create 99% confidence interval
# for population mean weight
st.norm.interval(alpha=0.99,
				loc=np.mean(gfg_data),
				scale=st.sem(gfg_data))
