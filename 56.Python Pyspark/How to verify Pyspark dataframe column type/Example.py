# importing necessary libraries
from pyspark.sql import SparkSession


# function to create new SparkSession
def create_session():
    spk = SparkSession.builder \
        .master("local") \
        .appName("Product_details.com") \
        .getOrCreate()

    return spk


def create_df(spark, data, schema):
    df1 = spark.createDataFrame(data, schema)
    return df1

if __name__ == "__main__":
    # calling function to create SparkSession
    spark = create_session()




    input_data = [("Mobile", 112345, 4.0, 12499),
              ("LED TV", 114567, 4.2, 49999),
              ("Refrigerator", 123543, 4.4, 13899),
              ("Washing Machine", 113465, 3.9, 6999),
              ("T-shirt", 124378, 4.1, 1999),
              ("Jeans", 126754, 3.7, 3999),
              ("Running Shoes", 134565, 4.7, 1499),
              ("Face Mask", 145234, 4.6, 999)]


    schema = ["Name", "ID", "Rating", "Price"]

    # calling function to create dataframe
    df = create_df(spark, input_data, schema)

    # visualizing the dataframe
    df.show()
