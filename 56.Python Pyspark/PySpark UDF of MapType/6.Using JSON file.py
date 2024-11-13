# Pyspark code to process json UDF
# Import necessary modules
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import MapType, StringType

# Create a SparkSession
spark = SparkSession.builder.getOrCreate()

# JSON data as a list of dictionaries
json_data = [
	{
		'name': 'John',
		'details': {
			'age': 25,
			'interests': ['reading', 'music'],
			'zip': '12345'
		},
		'date': '2023-06-30'
	},
	{
		'name': 'Jane',
		'details': {
			'age': 30,
			'interests': ['sports', 'movies'],
			'zip': '67890',
			'extra_info': {
				'height': 170,
				'weight': 60
			}
		},
		'date': '2023-06-30'
	}
]

# Create a DataFrame from the JSON data
df = spark.createDataFrame(json_data)

# Define a UDF to extract details from the map
def extract_details(details_map):
	age = details_map.get('age')
	interests = details_map.get('interests')
	zip_code = details_map.get('zip')
	return f"Age: {age}, Interests: {interests}, Zip Code: {zip_code}"

# Register the UDF
extract_details_udf = udf(extract_details, StringType())

# Apply the UDF to extract details from the map
df_with_details = df.withColumn('details_extracted', extract_details_udf(df['details']))

# Show specific details from the DataFrame
df_with_details.select('name', 'details_extracted', 'date').show(truncate=False)

# Stop the SparkSession
spark.stop()
