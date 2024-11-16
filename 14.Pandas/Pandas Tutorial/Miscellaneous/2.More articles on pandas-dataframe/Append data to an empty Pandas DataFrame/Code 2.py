# Appending a Data Frame of bool and bool
u = pd.DataFrame([[True, False]], columns =["A", "B"])
display(u)
display(u.dtypes)

t = t.append(u)
display(t)
display(t.dtypes) # type casted into float and float
