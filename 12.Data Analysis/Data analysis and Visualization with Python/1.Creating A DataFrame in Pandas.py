# assigning two series to s1 and s2
s1 = pd.Series([1,2])
s2 = pd.Series(["Ashish", "Sid"])
# framing series objects into data
df = pd.DataFrame([s1,s2])
# show the data frame
df

# data framing in another way
# taking index and column values
dframe = pd.DataFrame([[1,2],["Ashish", "Sid"]],
		index=["r1", "r2"],
		columns=["c1", "c2"])
dframe

# framing in another way
# dict-like container
dframe = pd.DataFrame({
		"c1": [1, "Ashish"],
		"c2": [2, "Sid"]})
dframe
