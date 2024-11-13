# importing necessary libraries
from pyspark.sql import SparkSession


# function to create new SparkSession
def create_session():
    spk = SparkSession.builder \
        .master("local") \
        .appName("Student_report.com") \
        .getOrCreate()

    return spk


def create_df(spark, data, schema):
    df1 = spark.createDataFrame(data, schema)
    return df1

if __name__ == "__main__":
    # calling function to create SparkSession
    spark = create_session()



    input_data = [(1, "Shivansh", "Male", 80, "Good Performance"),
              (2, "Arpita", "Female", 18, "Have to work hard otherwise "
                                          "result will not improve"),
              (3, "Raj", "Male", 21, "Work hard can do better"),
              (4, "Swati", "Female", 69, "Good performance can do more better"),
              (5, "Arpit", "Male", 20, "Focus on some subject to improve"),
              (6, "Swaroop", "Male", 65, "Good performance"),
              (7, "Reshabh", "Male", 70, "Good performance"),
              (8, "Dinesh", "Male", 65, "Can do better"),
              (9, "Rohit", "Male", 55, "Can do better"),
              (10, "Sanjana", "Female", 67, "Have to work hard")]



    schema = ["ID", "Name", "Gender", "Percentage", "Remark"]

    # calling function to create dataframe
    df = create_df(spark, input_data, schema)

    # visualizing full column content of the dataframe by setting truncate to 0
    df.show(truncate=0)
