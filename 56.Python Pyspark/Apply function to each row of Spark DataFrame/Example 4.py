from pyspark.sql.functions import udf
from pyspark.sql.types import StringType, StructType
from pyspark.sql.types import StructField
# Define Caesar Cipher UDF
@udf(StringType())
def caesar_cipher(text, shift):
	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	shifted_alphabet = alphabet[int(shift):]+ \
		alphabet[:int(shift)]
	table = str.maketrans(alphabet,
		shifted_alphabet)
	return text.translate(table)

# Define schema for DataFrame
schema = StructType([
	StructField('id', StringType(), True),
	StructField('text', StringType(), True),
	StructField('shift', StringType(), True)
])

# Create sample DataFrame
data = [
	('1', 'hello', '3'),
	('2', 'world', '5'),
	('3', 'goodbye', '10')
]

df = spark.createDataFrame(data, schema)

# Apply Caesar Cipher UDF to DataFrame
df = df.withColumn('ciphered_text',
			caesar_cipher(df['text'], df['shift']))

# Show results
df.show()
