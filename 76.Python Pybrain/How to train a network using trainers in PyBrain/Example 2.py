# Training the network with dataset nand_gate
trainer = BackpropTrainer(network, nand_gate)

# Iterate 100 times to train the network
for epoch in range(100):
	trainer.train()
	trainer.testOnData(dataset=nand_train, verbose = True)
