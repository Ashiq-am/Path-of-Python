# concatenating df1 and df2 along rows
vertical_concat = pd.concat([df1, df2], axis=0)

# concatinating df3 and df4 along columns
horizontal_concat = pd.concat([df3, df4], axis=1)

display(vertical_concat, horizontal_concat)
