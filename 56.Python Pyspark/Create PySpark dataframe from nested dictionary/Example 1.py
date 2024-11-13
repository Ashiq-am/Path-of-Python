# importing module
import pyspark

# importing sparksession from pyspark.sql module
from pyspark.sql import SparkSession
from pyspark.sql import Row

# creating sparksession and giving an app name
spark = SparkSession.builder.appName('sparkdf').getOrCreate()

# creating nested dictionary
data = {
	'student_1': {
		'student id': 7058,
		'country': 'India',
		'state': 'AP',
		'district': 'Guntur'
	},
	'student_2': {
		'student id': 7059,
		'country': 'Srilanka',
		'state': 'X',
		'district': 'Y'
	}
}

# taking row data
rowdata = [Row(**{'': k, **v}) for k,
		v in data.items()]

# creating the pyspark dataframe
final = spark.createDataFrame(rowdata).select(
'student id', 'country', 'state', 'district')

# display pyspark dataframe
final.show()
