# Appending a Data Frame of float and int
s = pd.DataFrame([[1.3, 9]], columns = ["A", "B"])
display(s)

# makes index continuous
t = t.append(s, ignore_index = True)
display(t)

# Resultant data frame is of type float and float
display(t.dtypes)
