# Import required module
from ifscApi.getDetails import FetchData

# Assign IFSC code
ifsc = 'KKBK0005652'

# Parse the ifsc code
data = FetchData().getdata(ifsc)

# Display details
print(data)
