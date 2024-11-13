# importing necessary libraries
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, LongType, StringType, FloatType


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

    input_data = [(("Refrigerator", 112345), 4.0, 12499),
                  (("LED TV", 114567), 4.2, 49999),
                  (("Washing Machine", 113465), 3.9, 69999),
                  (("T-shirt", 124378), 4.1, 1999),
                  (("Jeans", 126754), 3.7, 3999),
                  (("Running Shoes", 134565), 4.7, 1499),
                  (("Face Mask", 145234), 4.6, 999)]

    # defining schema for the dataframe using
    # nested StructType
    schm = StructType([
        StructField('Product', StructType([
            StructField('Product Name', StringType(), True),
            StructField('Product ID', LongType(), True),
        ])),

        StructField('Rating', FloatType(), True),
        StructField('Price', IntegerType(), True)])

    # calling function to create dataframe
    df = create_df(spark, input_data, schm)

    # visualizing dataframe and it's schema
    df.printSchema()
    df.show(truncate=False)
