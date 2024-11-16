# code
df1['QuantileRank']= pd.qcut(df1['EnglishScore'],
							q = 4, labels = False)
