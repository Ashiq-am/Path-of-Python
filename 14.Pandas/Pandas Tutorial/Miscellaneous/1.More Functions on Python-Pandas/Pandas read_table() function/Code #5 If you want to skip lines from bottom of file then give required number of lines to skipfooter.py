# importing pandas
import pandas as pd

pd.read_table('nba.csv',delimiter=',',index_col=0,
					engine='python',skipfooter=5)
