from pyspark.sql.functions import udf
from pyspark.sql.types import StructType, StructField
from pyspark.sql.types import StringType, FloatType
from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession

# Create a sample DataFrame
data = [("The Godfather", 1972,
		"Crime, Drama", 9.2),
		("The Shawshank Redemption",
		1994, "Drama", 9.3),
		("The Dark Knight", 2008,
		"Action, Crime, Drama", 9.0),
		("Pulp Fiction", 1994,
		"Crime, Drama", 8.9),
		("The Lord of the Rings: The Return of the King",
		2003, "Adventure, Drama, Fantasy", 8.9),
		("Forrest Gump", 1994, "Drama, Romance", 8.8),
		("Inception", 2010,
		"Action, Adventure, Sci-Fi", 8.8),
		("The Lord of the Rings: The Fellowship of the Ring",
		2001, "Adventure, Drama, Fantasy", 8.8),
		("The Lion King", 1994,
		"Animation, Adventure, Drama", 8.5),
		("The Matrix", 1999, "Action, Sci-Fi", 8.7)]

df = spark.createDataFrame(data, ["title", "year", "genre", "rating"])

# Define a function to remove movies with ratings less than 5
def filter_low_ratings(row):
	return row["rating"] >= 5

# Define a function to extract the decade from the year
def extract_decade(row):
	year = row["year"]
	decade = str(year // 10 * 10) + "s"
	return row + (decade, )

# Define a function to convert the genre to a list
def convert_to_list(row):
	genre = row["genre"]
	genre_list = genre.split(", ")
	return row + (genre_list, )

# Apply the functions to each row of the DataFrame
df.columns[0]
filtered_df = df.filter(filter_low_ratings(df))
decade_df = filtered_df.rdd.map(extract_decade).toDF(df.columns
							+ ["decade"])
list_df = decade_df.rdd.map(convert_to_list).toDF(df.columns +
						["decade", "genre_list"])

# Display the results
list_df.show()
