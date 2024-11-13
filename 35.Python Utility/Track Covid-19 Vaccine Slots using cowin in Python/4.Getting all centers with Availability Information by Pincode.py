from cowin_api import CoWinAPI
from pprint import pprint
cowin = CoWinAPI()

pin_code = "796014"
date = '14-05-2021'
min_age_limit = 18
available_centers = cowin.get_availability_by_pincode(pin_code, date)
print("All Available Centers [ By Pincode ] : ")
pprint(available_centers)
