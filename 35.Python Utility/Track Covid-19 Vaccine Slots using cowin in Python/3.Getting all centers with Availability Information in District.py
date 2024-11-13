from cowin_api import CoWinAPI
from pprint import pprint
cowin = CoWinAPI()

district_id = '425'
date = '14-05-2021'
available_centers = cowin.get_availability_by_district(district_id, date)
print("All Available Centers [ By district ] : ")
pprint(available_centers)
