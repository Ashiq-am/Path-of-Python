# creating a pipeline and
# droping the umwanted column
dropCol = pdp.ColDrop("index").apply(dataset)

# display the new dataframe
# after column drop
dropCol
