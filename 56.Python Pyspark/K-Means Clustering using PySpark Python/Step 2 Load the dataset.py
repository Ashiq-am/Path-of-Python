#Loading the data
dataset = spark.read.csv("seeds_dataset.csv",header=True,inferSchema=True)

#show the data in the above file using the below command
dataset.show(5)
