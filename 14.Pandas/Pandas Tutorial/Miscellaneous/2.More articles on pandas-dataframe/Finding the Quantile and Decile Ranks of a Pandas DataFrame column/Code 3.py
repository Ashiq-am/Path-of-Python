# code
df1['DecileRank']= pd.qcut(df1['EnglishScore'],
						q = 10, labels = False)
