# creating a pipeline and
# droping the umwanted column
dropCol2 = pdp.ColDrop("index")

# applying the ColDrop to dataframe
df2 = dropCol2(dataset)

# display dataframe
df2
