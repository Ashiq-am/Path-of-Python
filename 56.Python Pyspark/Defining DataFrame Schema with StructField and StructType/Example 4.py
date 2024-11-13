# importing necessary libraries
from pyspark.sql import SparkSession
import pyspark.sql.types as T
import json


# function to create SparkSession
def create_session():
    spk = SparkSession.builder \
        .master("local") \
        .appName("Product_mart.com") \
        .getOrCreate()
    return spk


# function to create dataframe
def create_df(spark, data, schema):
    df1 = spark.createDataFrame(data, schema)
    return df1


if __name__ == "__main__":
    # calling function to create SparkSession
    spark = create_session()

    input_data = [("Refrigerator", 4.0),
                  ("LED TV", 4.2),
                  ("Washing Machine", 3.9),
                  ("T-shirt", 4.1)
                  ]

    # defining schema for the dataframe with
    # StructType and StructField
    schm = T.StructType([
        T.StructField("Product Name", T.StringType(), True),
        T.StructField("Rating", T.FloatType(), True)
    ])

    # calling function to create dataframe
    df = create_df(spark, input_data, schm)

    # visualizing dataframe and it's schema
    print("Original Dataframe:-")
    df.printSchema()
    df.show()

    print("-------------------------------------------")
    print("Schema in json format:-")

    # storing schema in json format using
    # schema.json() function
    schma = df.schema.json()
    print(schma)

    # loading the json format schema
    schm1 = StructType.fromJson(json.loads(schma))

    # creating dataframe using json format schema
    json_df = spark.createDataFrame(
        spark.sparkContext.parallelize(input_data), schm1)
    print("-------------------------------------------")
    print("Dataframe using json schema:-")

    # showing the created dataframe from json format
    # schema printing the schema of created dataframe
    json_df.printSchema()
    json_df.show()
