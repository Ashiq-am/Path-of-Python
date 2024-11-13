import requests

IFSC_Code ='KKBK0005652'
URL = "https://ifsc.razorpay.com/"
result = requests.get(URL+IFSC_Code).json()
print(result)
