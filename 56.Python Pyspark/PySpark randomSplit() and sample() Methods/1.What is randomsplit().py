# import pyspark.sql for making tables
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("SparkByExamples.com").getOrCreate()

# make a table employee
emp = [(1, "Sagar", -1, "2018", "10", "M", 3000),
	(2, "G", 1, "2010", "20", "M", 4000),
	(3, "F", 1, "2010", "10", "M", 1000),
	(4, "G", 2, "2005", "10", "M", 2000),
	(5, "Great", 2, "2010", "40", "", -1),
	(6, "Hash", 2, "2010", "50", "", -1)]
# naming columns of employee table
empColumns = ["emp_id", "name", "superior_emp_id",
			"year_joined", "emp_dept_id", "gender", "salary"]
print("Employee Table")
# here, we have created a framework for table employee
empDF = spark.createDataFrame(data=emp, schema=empColumns)
empDF.printSchema()
empDF.show(truncate=False)

# make another table department
dept = [("F", 10), ("M", 20), ("S", 30), ("I", 40)]
print("Department Table")
# naming columns of department table
deptColumns = ["dept_name", "dept_id"]
# here, we have created a framework for table department
deptDF = spark.createDataFrame(data=dept, schema=deptColumns)
deptDF.printSchema()
deptDF.show(truncate=False)

print("- Inconsistencies on every run-")
# splitting up of data into two parts and joining one of them splitted part
# with department table in order to check the inconsistent behaviour of randomsplit
split1, split2 = empDF.randomSplit([0.5, 0.5])
print("Ist Run:", split1.join(
	deptDF, empDF.emp_dept_id == deptDF.dept_id, "inner").count())
split1, split2 = empDF.randomSplit([0.5, 0.5])
print("IInd Run:", split1.join(
	deptDF, empDF.emp_dept_id == deptDF.dept_id, "inner").count())
split1, split2 = empDF.randomSplit([0.5, 0.5])
print("IIIrd Run:", split1.join(
	deptDF, empDF.emp_dept_id == deptDF.dept_id, "inner").count())
split1, split2 = empDF.randomSplit([0.5, 0.5])
print("IVth Run:", split1.join(
	deptDF, empDF.emp_dept_id == deptDF.dept_id, "inner").count())
split1, split2 = empDF.randomSplit([0.5, 0.5])
print("Vth Run:", split1.join(
	deptDF, empDF.emp_dept_id == deptDF.dept_id, "inner").count())
