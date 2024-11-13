X = df.drop(["diagnosis", "id"],axis=1)
y= df['diagnosis']
y = y.map({'M':1, 'B':0})
