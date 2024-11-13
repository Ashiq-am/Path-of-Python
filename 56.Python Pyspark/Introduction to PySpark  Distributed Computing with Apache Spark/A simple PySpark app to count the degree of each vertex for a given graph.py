from pyspark import SparkConf, SparkContext
conf = SparkConf().setMaster("local").setAppName("Test")
# setMaster(local) - we are doing tasks on a single machine
sc = SparkContext(conf = conf)
def conv(line):
	line = line.split()
	return (int(line[0]), [int(line[1])])
def numNeighbours(x, y):
	return len(x) + len(y)
lines = sc.textFile('graph.txt')
edges = lines.map(lambda line: conv(line))
Adj_list = edges.reduceByKey(lambda x, y: numNeighbours(x, y))
print(Adj_list.collect())
