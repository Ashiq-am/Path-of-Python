from cowin_api import CoWinAPI
from pprint import pprint

cowin = CoWinAPI()

states = cowin.get_states()
print("All States List : ")
print(states)
