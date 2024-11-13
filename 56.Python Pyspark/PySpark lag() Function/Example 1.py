# PySpark - How to set the default
# value for pyspark.sql.functions
#.lag to a value within the current row?

# Import the SparkSession, Window and lag libraries
from pyspark.sql import SparkSession, Row
from pyspark.sql.window import Window
from pyspark.sql.functions import lag

# Create a spark session using getOrCreate() function
spark_session = SparkSession.builder.getOrCreate()

# Create a data frame using createDataFrame function
data_frame = spark_session.createDataFrame([Row(Serial_number=1,
												Brand='Maruti',
												Model='Suzuki'
											),
											Row(Serial_number=2,
												Brand='Hyundai',
												Model='Santro'
											),
											Row(Serial_number=3,
												Brand='Hyundai',
												Model='Venue')])

# Partition data through Brand column and sort it
# through Brand column in Window function
Windowspec = Window.partitionBy("Brand").orderBy("Brand")

# Calculating lag of brand by 1 for each student and using default
# value 'Any Other Brand' and putting in new column 'Updated Brand'
data_frame.withColumn('Updated Brand', lag(
	data_frame['Brand'], 1, 'Any Other Brand').over(Windowspec)).show()
