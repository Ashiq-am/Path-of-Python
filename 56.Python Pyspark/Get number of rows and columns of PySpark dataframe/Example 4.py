# importing necessary libraries
from pyspark.sql import SparkSession


# function to create SparkSession
def create_session():
    spk = SparkSession.builder \
        .master("local") \
        .appName("Student_report.com") \
        .getOrCreate()


    return spk


# function to create Dataframe
def create_df(spark, data, schema):
    df1 = spark.createDataFrame(data, schema)
    return df1

# main function
if __name__ == "__main__":
    # calling function to create SparkSession
    spark = create_session()


    input_data = [(1, "Shivansh", "Male", 20, 80),
              (2, "Arpita", "Female", 18, 66),
              (3, "Raj", "Male", 21, 90),
              (4, "Swati", "Female", 19, 91),
              (5, "Arpit", "Male", 20, 50),
              (6, "Swaroop", "Male", 23, 65),
              (7, "Reshabh", "Male", 19, 70),
              (8, "Dinesh", "Male", 20, 75),
              (9, "Rohit", "Male", 21, 85),
              (10, "Sanjana", "Female", 22, 87)]


    schm = ["Id", "Name", "Gender", "Age", "Percentage"]

    # calling function to create dataframe
    df = create_df(spark, input_data, schm)
    df.show()

    # converting PySpark df to Pandas df using
    # toPandas() function
    new_df = df.toPandas()

    # using Pandas shape function for getting the
    # dimension of the df
    dimension = new_df.shape

    # printing
    print("Dimension of the Dataframe is: ", dimension)
    print(f'Number of Rows are: {dimension[0]}')
    print(f'Number of Columns are: {dimension[1]}')
