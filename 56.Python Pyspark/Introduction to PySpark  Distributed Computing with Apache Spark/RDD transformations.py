# create an RDD called lines from ‘file_name.txt’
lines = sc.textFile("file_name.txt", 2)

# print lines.collect() prints the whole RDD
print(lines.collect())
