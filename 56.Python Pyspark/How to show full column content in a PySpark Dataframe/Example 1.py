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

    input_data = [("Mobile(Fluid Black, 8GB RAM, 128GB Storage)",
                   112345, 4.0, 12499),

                  ("LED TV", 114567, 4.2, 49999),

                  ("Refrigerator", 123543, 4.4, 13899),

                  ("6.5 kg Fully-Automatic Top Loading Washing Machine \
				(WA65A4002VS/TL, Imperial Silver, Center Jet Technology)",
                   113465, 3.9, 6999),

                  ("T-shirt", 124378, 4.1, 1999),

                  ("Jeans", 126754, 3.7, 3999),

                  ("Men's Casual Shoes in White Sneakers for Outdoor and\
				Daily use", 134565, 4.7, 1499),

                  ("Vitamin C Ultra Light Gel Oil-Free Moisturizer",
                   145234, 4.6, 999),
                  ]

    schema = ["Name", "ID", "Rating", "Price"]

    # calling function to create dataframe
    df = create_df(spark, input_data, schema)

    # visualizing full content of the Dataframe
    # by setting truncate to False
    df.show(truncate=False)
