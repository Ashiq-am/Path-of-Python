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

    input_data = [(1, "Shivansh", "Male", (70, 66, 78, 70, 71, 50), 80,
                   "Good Performance"),

                  (2, "Arpita", "Female", (20, 16, 8, 40, 11, 20), 18,
                   "Have to work hard otherwise result will not improve"),

                  (3, "Raj", "Male", (10, 26, 28, 10, 31, 20),
                   21, "Work hard can do better"),

                  (4, "Swati", "Female", (70, 66, 78, 70, 71, 50),
                   69, "Good performance can do more better"),

                  (5, "Arpit", "Male", (20, 46, 18, 20, 31, 10),
                   20, "Focus on some subject to improve"),

                  (6, "Swaroop", "Male", (70, 66, 48, 30, 61, 50),
                   65, "Good performance"),

                  (7, "Reshabh", "Male", (70, 66, 78, 70, 71, 50),
                   70, "Good performance"),

                  (8, "Dinesh", "Male", (40, 66, 68, 70, 71, 50),
                   65, "Can do better"),

                  (9, "Rohit", "Male", (50, 66, 58, 50, 51, 50),
                   55, "Can do better"),

                  (10, "Sanjana", "Female", (60, 66, 68, 60, 61, 50),
                   67, "Have to work hard")]

    schema = ["ID", "Name", "Gender",
              "Sessionals Marks", "Percentage", "Remark"]

    # calling function to create dataframe
    df = create_df(spark, input_data, schema)

    # visualizing full column content of the
    # datframe by setting n and truncate to
    # False
    df.show(df.count(), truncate=False)
