# using categories attribute
c6 = pd.Categorical([1, 2, 3, 1, 2, 3], categories = [4, 1, 3, 5])
print ("\nc6 : ", c6)

print("\n\nSeries : \n", pd.Series(c6))

df = pd.DataFrame({"A":[1, 2, 3, 1, 2, 3]})
df["B"] = c6
print ("\n\nDataframe : \n", df)
