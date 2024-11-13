sea = sns.FacetGrid(exercise, col = "time",
					height = 4, aspect =.5)

sea.map(sns.barplot, "diet", "pulse",
		order = ["no fat", "low fat"])
