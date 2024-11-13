# function to get data from api
def casesData():
	# getting the json data by calling api
	data = ((requests.get(url)).json())
	states = []

	# getting states
	for key in data.items():
		states.append(key[0])

	# getting statewise data
	for state in states:
		f = (data[state]['districtData'])
		tc = []
		dis = []
		act, con, dea, rec = 0, 0, 0, 0

		# getting districtwise data
		for key in (data[state]['districtData']).items():
			district = key[0]
			dis.append(district)
			active = data[state]['districtData'][district]['active']
			confirmed = data[state]['districtData'][district]['confirmed']
			deaths = data[state]['districtData'][district]['deceased']
			recovered = data[state]['districtData'][district]['recovered']
			if district == 'Unknown':
				active, confirmed, deaths, recovered = 0, 0, 0, 0
			tc.append([active, confirmed, deaths, recovered])
			act = act + active
			con = con + confirmed
			dea = dea + deaths
			rec = rec + recovered
		tc.append([act, con, dea, rec])
		dis.append('Total')
		parameters = ['Active', 'Confirmed', 'Deaths', 'Recovered']

		# creating a dataframe
		df = pd.DataFrame(tc, dis, parameters)
		print('COVID - 19', state, 'District Wise Data')
		print(df)

		# plotting of data
		plt.bar(dis, df['Active'], width=0.5, align='center')
		fig = plt.gcf()
		fig.set_size_inches(18.5, 10.5)
		plt.xticks(rotation = 75)
		plt.show()
		print('*' * 100)
