df1 = df[(df.Class == 8) & ((df.English<=5) | (df.Maths>5) | (df.History<=5))]
print(df1)
