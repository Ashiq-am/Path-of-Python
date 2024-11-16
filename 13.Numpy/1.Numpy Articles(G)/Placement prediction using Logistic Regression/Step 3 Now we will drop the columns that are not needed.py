# dropping the serial no and salary col
dataset = dataset.drop('sl_no', axis=1)
dataset = dataset.drop('salary', axis=1)
