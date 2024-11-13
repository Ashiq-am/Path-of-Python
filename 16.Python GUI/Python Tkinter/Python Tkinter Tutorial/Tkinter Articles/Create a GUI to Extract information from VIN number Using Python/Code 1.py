# importing module
from vininfo import Vin

# Pass the VIN number into Vin methods
vin = Vin('MAJGERTYKGHG56037')

# prints vehicle's country
print(vin.country)

# prints vehicle's manufacturer
print(vin.manufacturer)

# prints vehicle manufacturer's region
print(vin.region)
