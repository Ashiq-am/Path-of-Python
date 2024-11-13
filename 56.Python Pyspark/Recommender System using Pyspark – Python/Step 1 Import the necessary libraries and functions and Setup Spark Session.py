#importing the required pyspark library
from pyspark.sql import SparkSession
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.recommendation import ALS

#Setup Spark Session
spark = SparkSession.builder.appName('Recommender').getOrCreate()
spark
