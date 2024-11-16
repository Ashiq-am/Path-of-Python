# Mixed categories
c4 = pd.Categorical(['a', 2, 3, 1, 2, 3])
print ("\nc4 : ", c4)

c5 = pd.Categorical(['a', 2, 3, 1, 2, 3], ordered = True)
print ("\nc5 : ", c5)
