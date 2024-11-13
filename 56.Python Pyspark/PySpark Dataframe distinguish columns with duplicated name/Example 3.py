# Import the libraries SparkSession
from pyspark.sql import SparkSession

# Create a spark session using getOrCreate() function
spark_session = SparkSession.builder.getOrCreate()

# Read the CSV file
df=csv_file = spark_session.read.csv(
'/content/currency_prices.csv',
sep = ',', inferSchema = True, header = True)

# Store all the column names in the list
df_cols=df.columns

# Create loop to remove extra charcters got in
# the column names while importing CSV file
for i in range(len(df_cols)):

    if df_cols[i][-1].isdigit():
        m=df_cols[i][:-1]
        df_cols[i]=m

# Rename the duplicate columns in data frame
df=df.toDF(*df_cols)

duplicate_col_index = [idx for idx,
val in enumerate(df_cols) if val in df_cols[:idx]]

# Create a new list by renaming duplicate
# columns by adding prefix '_duplicate_'+index
for i in duplicate_col_index:
    df_cols[i] = df_cols[i] + '_duplicate_'+ str(i)

# Rename the duplicate columns in data frame
df = df.toDF(*df_cols)

# Define a function to do sum
average_price=lambda a,b,c,d: (a+b+c+d)/4

# Display the data frame with new column calling
# the average_price function with prices as arguments
df.withColumn('Average Price',
		average_price(df.price,
						df.price_duplicate_2,
						df.price_duplicate_3,
						df.price_duplicate_4) ).show()
