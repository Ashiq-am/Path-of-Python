# importing necessary libraries
from pyspark.sql import SparkSession


# function to create new SparkSession
def create_session():
    spk = SparkSession.builder \
        .master("local") \
        .appName("Filter_values.com") \
        .getOrCreate()
    return spk


def create_df(spark, data, schema):
    df1 = spark.createDataFrame(data, schema)
    return df1


if __name__ == "__main__":
    # calling function to create SparkSession
    spark = create_session()

    input_data = [("Shivansh", "Data Scientist", "Noida"),
                  (None, "Software Developer", None),
                  ("Swati", "Data Analyst", "Hyderabad"),
                  (None, None, "Noida"),
                  ("Arpit", "Android Developer", "Banglore"),
                  (None, None, None)]

    schema = ["Name", "Job Profile", "City"]

    # calling function to create dataframe
    df = create_df(spark, input_data, schema)

    # filtering the columns with None values
    df = df.filter("City is Not NULL")

    # visulizing the dataframe
    df.show()
