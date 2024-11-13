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
              (6, "Swaroop", "Male", 23, 65),
              (6, "Swaroop", "Male", 23, 65),
              (7, "Reshabh", "Male", 19, 70),
              (7, "Reshabh", "Male", 19, 70),
              (8, "Dinesh", "Male", 20, 75),
              (9, "Rohit", "Male", 21, 85),
              (9, "Rohit", "Male", 21, 85),
              (10, "Sanjana", "Female", 22, 87)]



    schm = ["Id", "Name", "Gender", "Age", "Percentage"]

    # calling function to create dataframe
    df = create_df(spark, input_data, schm)
    df.show()

    # extracting number of distinct rows
    # from the Dataframe
    row = df.distinct().count()

    # extracting total number of rows from
    # the Dataframe
    all_rows = df.count()

    # extracting number of columns from the
    # Dataframe
    col = len(df.columns)

    # printing
    print(f'Dimension of the Dataframe is: {(row, col)}')
    print(f'Distinct Number of Rows are: {row}')
    print(f'Total Number of Rows are: {all_rows}')
    print(f'Number of Columns are: {col}')
