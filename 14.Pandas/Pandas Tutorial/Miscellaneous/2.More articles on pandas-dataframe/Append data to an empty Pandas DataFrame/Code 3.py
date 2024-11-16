# Appending a Data Frame of object and object
x = pd.DataFrame([["1.3", "9.2"]], columns = ["A", "B"])
display(x)
display(x.dtypes)

t = t.append(x)
display(t)
display(t.dtypes)
