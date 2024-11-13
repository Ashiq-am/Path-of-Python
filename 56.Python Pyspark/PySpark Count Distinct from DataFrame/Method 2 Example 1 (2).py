# importing countDistinct from
# pyspark.sql.functions
from pyspark.sql.functions import countDistinct

# applying the function countDistinct()
# on df using select()
df3 = df.select(countDistinct("Depart"))

# show df2
df3.show()
