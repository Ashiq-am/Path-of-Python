# Import required modules
from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder.appName("Split DataFrame").getOrCreate()

# Load the data into a DataFrame
df = spark.read.csv("number.csv",
					header=True,
					inferSchema=True)

# Split the DataFrame into two
# data frame based on a condition
males_df = df.filter(df['gender'] == 'Male')
females_df = df.filter(df['gender'] == 'Female')

# Print the data frames
males_df.show()
females_df.show()

# Print the count
print("Males:", males_df.count())
print("Females:", females_df.count())
