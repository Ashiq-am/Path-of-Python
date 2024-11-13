import json
import pandas as pd

while (1):
	print("Choose Any One of The Following :- ")
	print("1)Admin")
	print("2)User")
	print("3)Exit")
	print("Enter Your Choice Here :- ")
	n = int(input())
	if (n == 1):
		admin()
	elif (n == 2):
		user()
	elif (n == 3):
		break
	else:
		print("Invalid Choice...!!!")
