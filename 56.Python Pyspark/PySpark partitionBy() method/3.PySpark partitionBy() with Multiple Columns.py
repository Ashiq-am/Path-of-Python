# From above DataFrame, we will be using
# Team and Speciality as a partition key
# for our examples below.
# partitionBy()
df.write.option("header", True) \
		.partitionBy("Team", "Speciality") \
		.mode("overwrite") \
		.csv("Team-Speciality")

# change directory
#cd Team = Ind
#cd Team-Speciality
#cd Team = Ind
#ls
