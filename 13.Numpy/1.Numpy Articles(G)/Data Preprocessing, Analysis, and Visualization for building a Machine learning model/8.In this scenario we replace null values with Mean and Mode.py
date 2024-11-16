dataset["Geography"].fillna(dataset["Geography"].mode()[0],inplace = True)
dataset["Gender"].fillna(dataset["Gender"].mode()[0],inplace = True)
dataset["Age"].fillna(dataset["Age"].mean(),inplace = True)
