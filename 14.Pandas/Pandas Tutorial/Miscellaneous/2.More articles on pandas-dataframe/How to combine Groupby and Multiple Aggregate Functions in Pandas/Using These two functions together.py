# find an aggregation of column "beer_servings"
# by grouping the "continent" column.
df.groupby(df["continent"]).beer_servings.agg(["min",
											"max",
											"sum",
											"count",
											"mean"])
