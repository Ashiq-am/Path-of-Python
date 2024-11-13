# importing necessary libraries
from pyspark.sql import SparkSession

# function to create new SparkSession
def create_session():

    spk = SparkSession.builder \
        .master("local") \
        .appName("Geek_examples.com") \
        .getOrCreate()

    return spk

# main function
if __name__ == "__main__":
    # calling function to create SparkSession
    spark = create_session()

    # creating dataframe using createDataFrame()
    # function in which pass data and schema
    df = spark.createDataFrame([
        ("Mazda RX4",21,4,4),
        ("Hornet 4 Drive",22,3,2),
        ("Merc 240D",25,4,2),
        ("Lotus Europa",31,5,2),
        ("Ferrari Dino",20,5,6),
        ("Volvo 142E",22,4,2)
    ],["Car Name","mgp","gear","carb"])

    # visualizing the dataframe using show() function
    df.show()
