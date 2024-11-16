dataframe['Change'] = dataframe.A.div(dataframe.A.shift())
dataframe['Change'].plot(figsize=(15, 10),
						xlabel = "Date",
						ylabel = "Value Difference",
						title = "Shift Plot")
