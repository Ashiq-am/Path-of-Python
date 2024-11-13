# Import required modules
import requests

# Assign IFSC code and URL
IFSC_Code = 'KKBK0005652'
URL = "https://ifsc.razorpay.com/"

# Use get() method
data = requests.get(URL+IFSC_Code).json()

# Display bank details
print(data)
