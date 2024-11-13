exercise_kind = exercise.kind.value_counts().index
sea = sns.FacetGrid(exercise, row = "kind",
					row_order = exercise_kind,
					height = 1.7, aspect = 4)

sea.map(sns.kdeplot, "id")
