# Import required modules
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
from pyspark.sql.functions import lit

from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder.appName("Metadata").getOrCreate()
from pyspark.sql.functions import lit
import json

# Create a DataFrame
data = [("Alice", 25),
        ("Bob", 30),
        ("Charlie", 35)]
df = spark.createDataFrame(data,
                           ["name", "age"])
df.printSchema()


# Define a function to update the metadata
def withMetadata(df, metadata):
    # Update the metadata of the DataFrame
    df = df.withColumnRenamed("name",
                              "username")
    df = df.withColumn("age",
                       df["age"].cast("double"))
    df = df.withColumn("gender",
                       lit("unknown"))
    df = df.drop("gender")
    fields = [StructField(field.name,
                          field.dataType,
                          False) for field in df.schema.fields]
    new_schema = StructType(fields)
    df = spark.createDataFrame(df.rdd,
                               new_schema)

    # Add the metadata to the DataFrame
    df = df.withColumn("metadata",
                       lit(json.dumps(metadata)))
    return df


# Update the metadata of the DataFrame
df = withMetadata(df, {"source": "file",
                       "date": "2022-01-01"})
df.printSchema()
