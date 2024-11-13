# Sort the dataframe by descending order
# of 'Job' and whenever there is conflict
# in 'Job', it'll be resolved by ordering
# based on ascending order of 'Salary'
df.orderBy(f.col("Job").desc(),f.col("Salary").asc()).show()

# or
# df.orderBy(["Job", "Salary"],ascending = [False, True]).show()
