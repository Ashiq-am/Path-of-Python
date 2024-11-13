#select first and second column
# to get unique data using dropDuplicates function()
dataframe.select(["Employee ID",
				"Employee NAME"]).dropDuplicates().show()
