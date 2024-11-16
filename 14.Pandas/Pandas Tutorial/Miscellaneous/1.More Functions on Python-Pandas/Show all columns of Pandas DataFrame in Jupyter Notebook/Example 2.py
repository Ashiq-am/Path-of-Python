#import pandas
import pandas as pd

# read csv
df = pd.read_csv('data.csv')

# set max_colwidth to 3000
pd.set_option('display.max_colwidth', 3000)
