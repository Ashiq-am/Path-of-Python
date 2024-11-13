@udf(returnType=StringType())
def Converter(str):
    result = ""
    a = str.split(" ")

    for q in a:
        if q == 'J' or 'C' or 'M':
            result += q[1:2].upper()
        else:
            result += q
    return result


df.withColumn("Special Names", Converter("Name")) \
    .show()
