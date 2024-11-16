import pandas as pd


df = pd.DataFrame([('Bike', 'Kawasaki', 186),
				('Bike', 'Ducati Panigale', 202),
				('Car', 'Bugatti Chiron', 304),
				('Car', 'Jaguar XJ220', 210),
				('Bike', 'Lightning LS-218', 218),
				('Car', 'Hennessey Venom GT', 270),
				('Bike', 'BMW S1000RR', 188)],
				columns =('Type', 'Name', 'top_speed(mph)'))

df
