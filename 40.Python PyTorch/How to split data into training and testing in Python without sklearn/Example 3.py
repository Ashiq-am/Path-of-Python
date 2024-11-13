# Select ratio
ratio = 0.75

total_rows = df.shape[0]
train_size = int(total_rows*ratio)

# Split data into test and train
train = df[0:train_size]
test = df[train_size:]
