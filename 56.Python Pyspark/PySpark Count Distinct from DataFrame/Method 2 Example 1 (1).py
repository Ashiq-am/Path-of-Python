# importing countDistinct from
# pyspark.sql.functions
from pyspark.sql.functions import countDistinct

# applying the function countDistinct()
# on df using select()
df2 = df.select(countDistinct("Emp_name", "Depart", "Salary"))

# show df2
df2.show()
