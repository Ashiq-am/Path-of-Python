# Import required modules
from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder.appName("Split DataFrame").getOrCreate()

# Load the data into a DataFrame
df = spark.read.csv("number.csv",
					header=True,
					inferSchema=True)
df.show()

# Split the DataFrame into two
# DataFrames based on a condition
males_df = df.filter(df['gender'] == 'Male')
females_df = df.filter(df['gender'] == 'Female')

# Print the dataframes
males_df.show()
females_df.show()
