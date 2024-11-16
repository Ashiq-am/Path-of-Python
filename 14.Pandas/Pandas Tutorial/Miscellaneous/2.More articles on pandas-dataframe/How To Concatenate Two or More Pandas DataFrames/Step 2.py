df1 = pd.DataFrame(np.random.randint(25, size=(4, 4)),
				index=["1", "2", "3", "4"],
				columns=["A", "B", "C", "D"])

df2 = pd.DataFrame(np.random.randint(25, size=(6, 4)),
				index=["5", "6", "7", "8", "9", "10"],
				columns=["A", "B", "C", "D"])

df3 = pd.DataFrame(np.random.randint(25, size=(4, 4)),
				columns=["A", "B", "C", "D"])

df4 = pd.DataFrame(np.random.randint(25, size=(4, 4)),
				columns=["E", "F", "G", "H"])

display(df1, df2, df3, df4)
