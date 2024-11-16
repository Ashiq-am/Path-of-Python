# importing pandas as pd
import pandas as pd

# Creating the index and setting the name
pd.Index(['Beagle', 'Pug', 'Labrador', 'Pug',
'Mastiff', None, 'Beagle']).set_names('Dog_breeds')
