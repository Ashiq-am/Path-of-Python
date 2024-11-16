# import pandas module
import pandas as pd

# import numpy module
import numpy as np

# create dataframe with 3 columns
data = pd.DataFrame({

	"name": ['sravan', np.nan, 'harsha', 'ramya'],
	"subjects": [np.nan, 'java', np.nan, 'html/php'],
	"marks": [98, np.nan, np.nan, np.nan]
})

# replace nan with empty string
# using replace() function
data.replace(np.nan, '')
