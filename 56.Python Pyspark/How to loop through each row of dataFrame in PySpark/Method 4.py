# importing necessary libraries
import pyspark
from pyspark.sql import SparkSession


# function to create new SparkSession
def create_session():
    spk = SparkSession.builder \
        .master("local") \
        .appName("employee_profile.com") \
        .getOrCreate()


    return spk


def create_df(spark, data, schema):
    df1 = spark.createDataFrame(data, schema)
    return df1

if __name__ == "__main__":
    # calling function to create SparkSession
    spark = create_session()



    input_data = [(1, "Shivansh", "Data Scientist", 2000000, "Noida"),
              (2, "Rishabh", "Software Developer", 1500000, "Banglore"),
              (3, "Swati", "Data Analyst", 1000000, "Hyderabad"),
              (4, "Amar", "Data Analyst", 950000, "Noida"),
              (5, "Arpit", "Android Developer", 1600000, "Pune"),
              (6, "Ranjeet", "Python Developer", 1800000, "Gurugram"),
              (7, "Priyanka", "Full Stack Developer", 2200000, "Banglore")]


    schema = ["Id", "Name", "Job Profile", "Salary", "City"]

    # calling function to create dataframe
    df = create_df(spark, input_data, schema)

    # map() is only be performed on rdd
    # so converting the dataframe into rdd using df.rdd
    rdd = df.rdd.map(lambda loop: (
    loop["Id"], loop["Name"], loop["Salary"], loop["City"])
                 )

    # after looping the getting the data from each row
    # converting back from RDD to Dataframe
    df2 = rdd.toDF(["Id", "Name", "Salary", "City"])

    # showing the new Dataframe
    df2.show()
