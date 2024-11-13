from cowin_api import CoWinAPI
from pprint import pprint


cowin = CoWinAPI()
state_id = '24'
districts = cowin.get_districts(state_id)

print("Districts by State Id : ")
pprint(districts)
