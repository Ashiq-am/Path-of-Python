# importing the modules
import numpy as np
import pandas as pd

# creating the DataFrame
dictionary = {'Names': ['Simon', 'Josh', 'Amen',
						'Habby', 'Jonathan', 'Nick', 'Jake'],
			'Capitals': ['VIENNA', np.nan, 'BRASILIA',
						np.nan, 'PARIS', 'DELHI', 'BERLIN'],
			'Countries': ['AUSTRIA', 'BELGIUM', 'BRAZIL',
							np.nan, np.nan, 'INDIA', np.nan]}
table = pd.DataFrame(dictionary, columns = ['Names',
										'Capitals',
										'Countries'])

# displaying the DataFrame
display(table)
