#import the packages
import pandas as pd
import pandas_profiling

# read the file
df = pd.read_csv('Geeks.csv')

# run the profile report
profile = df.profile_report(title='Pandas Profiling Report')
