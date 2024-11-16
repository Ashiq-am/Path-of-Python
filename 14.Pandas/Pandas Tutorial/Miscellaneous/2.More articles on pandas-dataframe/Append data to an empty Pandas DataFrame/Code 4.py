# Creating a DataFrame using a for loop in efficient manner
y = pd.concat([pd.DataFrame([[i, i * 10]], columns = ["A", "B"])
			for i in range(7, 10)], ignore_index = True)

# makes index continuous
t = t.append(y, ignore_index = True)
display(t)
display(t.dtypes)
