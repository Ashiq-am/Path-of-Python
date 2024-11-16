#import pandas
import pandas as pd

# read csv file
df = pd.read_csv('data.csv')

# replacing values
df['Education'].replace(['Under-Graduate', 'Diploma '],
						[0, 1], inplace=True)
