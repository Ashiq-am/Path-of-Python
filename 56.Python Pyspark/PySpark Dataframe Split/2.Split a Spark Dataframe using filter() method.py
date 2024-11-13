import pyspark
import pandas as pd

session = pyspark.sql.SparkSession.builder.getOrCreate()

# making DataFrame in Pandas and
# converting ot to a PySpark DataFrame.
df = pd.DataFrame({
	'Odd_Numbers':[y for y in range(1,
							17, 2)],
	'Even_Numbers':[x for x in range(2,
							17, 2)],
})

df = session.createDataFrame(df)

print("Original Data frame")
df.show()

# split Dataframes
print("Splitted Dataframe")
df.filter(df['Odd_Numbers'] < 10).show()
df.filter(df['Odd_Numbers'] > 10).show()
