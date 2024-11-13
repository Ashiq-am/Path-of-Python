df.write.option("header", True) \
		.partitionBy("Team") \
		.mode("overwrite") \
		.csv("Team")

# change directory
#cd Team

# On our DataFrame, we have a total
# of 9 different teams hence,
# it creates 9 directories as shown below.
# The name of the sub-directory would be
# the partition column and its value
# (partition column=value).
#ls
