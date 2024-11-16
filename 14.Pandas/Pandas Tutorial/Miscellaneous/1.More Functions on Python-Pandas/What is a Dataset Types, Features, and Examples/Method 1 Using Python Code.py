import pandas as pd
import numpy as np
import random as rd

#Bussiness_type = ['Office_space','Restaurants','Textile_shop','Showrooms','grocery_shop']
Bussiness_type = [1, 2, 3, 4, 5]
#Demographics = ['Kids', 'Youth', 'Midde_aged', 'Senior']
Demographics = [1, 2, 3, 4]
#Accessibility = ['Bad', 'Fair', 'Good', 'Excellent']
Accessibility = [1, 2, 3, 4]
#Competition = ['low', 'medium', 'high']
Competition = [1, 2, 3]
Area = [250, 500, 750, 1000, 1500]
Rent_per_month = ['5000', '75000', '95000', '10000', '13000', '17000', '20000']
Gross_tax = [2.2, 3.4, 4.5, 5.6, 7.2, 10.2, 6.8, 9.3, 11, 13.4]
labour_cost = [3500, 5000, 6500, 7500, 9000, 11000, 16000, 25000, 15000, 12500]
location = ['San Diego', 'Miami', 'Seattle', 'LosAngeles', 'LasVegas', 'Idaho', 'Phoenix', 'New Orleans',
			'WashingtionDC', 'Chicago', 'Boston', 'Philadelphia', 'New York', 'San Jose', 'Detroit', 'Dallas']
#location = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

buss_type = []
demo = []
access = []
comp = []
area = []
rpm = []
gtax = []
labour_cst = []
loc = []

# Net_profit is to be calculated

for i in range(1000):
	buss_type.append(rd.choice(Bussiness_type))
	demo.append(rd.choice(Demographics))
	access.append(rd.choice(Accessibility))
	comp.append(rd.choice(Competition))
	area.append(rd.choice(Area))
	rpm.append(rd.choice(Rent_per_month))
	gtax.append(rd.choice(Gross_tax))
	labour_cst.append(rd.choice(labour_cost))
	loc.append(rd.choice(location))


dic_data = {'Business_type': buss_type, 'Demographics': demo, 'Accessibility': access, 'Competition': comp,
			'Area(sq feet)': area, 'Rent_per_month': rpm, 'Gross_tax(%)': gtax, 'labour_cost(USD)': labour_cst, 'location': loc}
frame_data = pd.DataFrame(dic_data)
frame_data.to_csv('autogen_data.csv')
