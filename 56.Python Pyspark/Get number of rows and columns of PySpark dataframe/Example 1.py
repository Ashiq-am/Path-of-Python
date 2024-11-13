# importing necessary libraries
from pyspark.sql import SparkSession


# function to create SparkSession
def create_session():
    spk = SparkSession.builder \
        .master("local") \
        .appName("Products.com") \
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



    input_data = [(1, "Direct-Cool Single Door Refrigerator", 12499),
              (2, "Full HD Smart LED TV", 49999),
              (3, "8.5 kg Washing Machine", 69999),
              (4, "T-shirt", 1999),
              (5, "Jeans", 3999),
              (6, "Men's Running Shoes", 1499),
              (7, "Combo Pack Face Mask", 999)]



    schm = ["Id", "Product Name", "Price"]

    # calling function to create dataframe
    df = create_df(spark, input_data, schm)
    df.show()

    # extracting number of rows from the Dataframe
    row = df.count()

    # extracting number of columns from the Dataframe
    col = len(df.columns)

    # printing
    print(f'Dimension of the Dataframe is: {(row, col)}')
    print(f'Number of Rows are: {row}')
    print(f'Number of Columns are: {col}')
