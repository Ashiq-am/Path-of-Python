# Creating a dataset for testing
nand_train = SupervisedDataSet(2, 1)



# Fit input and target values to dataset
# Parameters for nand_train truth table
nand_train.addSample((0, 0), (1,))
nand_train.addSample((0, 1), (0,))
nand_train.addSample((1, 0), (1,))
nand_train.addSample((1, 1), (0,))
