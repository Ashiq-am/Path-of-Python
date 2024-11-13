# importing necessary libraries
from pyspark.sql import SparkSession


# function to create new SparkSession
def create_session():
    spk = SparkSession.builder \
        .appName("Corona_cases_statewise.com") \
        .getOrCreate()


    return spk


# function to create RDD
def create_RDD(sc_obj, data):
    df = sc.parallelize(data)
    return df


# function to convert RDD to dataframe
def RDD_to_df(spark, df, schema):
    # converting RDD to df using createDataframe()
    # in which we are passing RDD and schema of df
    df1 = spark.createDataFrame(df, schema)
    return df1

if __name__ == "__main__":


    input_data = [("Uttar Pradesh", 122000, 89600, 12238),
              ("Maharashtra", 454000, 380000, 67985),
              ("Tamil Nadu", 115000, 102000, 13933),
              ("Karnataka", 147000, 111000, 15306),
              ("Kerala", 153000, 124000, 5259)]

    # calling function to create SparkSession
    spark = create_session()

    # creating spark context object
    sc = spark.sparkContext

    # calling function to create RDD
    rd_df = create_RDD(sc, input_data)



    schema_lst = ["State", "Cases", "Recovered", "Deaths"]

    # calling function to covert RDD to dataframe
    converted_df = RDD_to_df(spark, rd_df, schema_lst)

    # visualizing the schema and dataframe
    converted_df.printSchema()
    converted_df.show()
