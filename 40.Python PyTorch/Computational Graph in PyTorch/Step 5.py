# Pooling layer
pool = net.pool
print('pooling Layer :',pool)

# APPLY THE Pooling layer to the
# output of FIRST Convolutional layer
y2 = pool(y1)
print('Output Shape :',y2.shape)

# Computational Graph
make_dot(y2, params=dict(net.named_parameters()))
