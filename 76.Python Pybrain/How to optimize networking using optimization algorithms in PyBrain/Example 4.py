# 100 iterations for learning
for i in range(100):
	myNetwork = gaOptimization.learn(0)[0]

# Giving input to activate the network
print(myNetwork.activate([0, 0]))
print(myNetwork.activate([1, 0]))
print(myNetwork.activate([0, 1]))
print(myNetwork.activate([1, 1]))
