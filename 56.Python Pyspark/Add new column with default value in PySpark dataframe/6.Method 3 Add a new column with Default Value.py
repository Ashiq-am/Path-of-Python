# Add columns to DataFrame using SQL
df.createOrReplaceTempView("GFG_Table")

# Add new column with NUll
df=spark.sql("select *, null as Rewards from GFG_Table")

# Add new constanst column
df.createOrReplaceTempView("GFG_Table")
df=spark.sql("select *, '0.25' as Bonus_Percent from GFG_Table")
df.show()
