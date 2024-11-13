# partitionBy() control number of partitions
df.write.option("header",True) \
		.option("maxRecordsPerFile", 2) \
		.partitionBy("Team") \
		.mode("overwrite") \
		.csv("Team")



# change directory
#cd Team
#ls
