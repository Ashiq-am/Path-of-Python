c1 = pd.Series(['a', 'b', 'a', 'e'], dtype = c)
print ("c1 : \n", c1)


c2 = pd.DataFrame({'A': list('abca'), 'B': list('bccd')})

c3 = CategoricalDtype(categories=list('abcd'), ordered=True)

c4 = c2.astype(c3)

print ("\n c4['A'] : \n", c4['A'])
