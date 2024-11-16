# importing pandas
import pandas as pd

pd.read_table('nba.csv',delimiter=',',index_col=0,header=[1,3,5])
