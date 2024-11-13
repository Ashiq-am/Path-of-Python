sea = sns.FacetGrid(exercise, row = "diet",
					col = "time", margin_titles = True)

sea.map(sns.regplot, "id", "pulse", color = ".3",
		fit_reg = False, x_jitter = .1)
