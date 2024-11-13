import numpy as np

# Define a list of data types to test casting
data_types = [np.int32,np.float64,complex,'i8','f8','i4','S4']

# Perform casting checks for each pair of data types
for i in range(len(data_types)):
    for j in range(i+1, len(data_types)):
        source_type = data_types[i]
        destination_type = data_types[j]
        res = np.can_cast(source_type, destination_type)
        print(f"Can cast {source_type} to {destination_type}: {res}")
